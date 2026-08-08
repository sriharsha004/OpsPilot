# LLM Fundamentals

Notes from Jul 27 (roadmap day: Gemini mental model). Written to build intuition for
what LLM calls in OpsPilot can and can't rely on — not a general ML primer.

## Tokens

A token is the unit an LLM actually reads and generates — not the same as a word or a
character. Roughly ¾ of a word in English on average; a word like "preschool" might
split into two tokens ("pre" + "school"). API usage is priced and rate-limited by
token count (input + output combined), not by character or word count. This matters
for OpsPilot directly: any prompt that includes lead history or documents needs to be
sized in tokens, not words, or we'll misjudge cost and hit limits unexpectedly.

## How the model predicts the next token

At each step, the model looks at the sequence of tokens so far and outputs a
probability distribution over every possible next token in its vocabulary. It samples
one token from that distribution, appends it to the sequence, and repeats — one token
at a time, feeding its own output back in as the next input. There's no planning
ahead to a full sentence; each token is chosen with only the tokens before it as
context.

## Why outputs are probabilistic

The next-token choice isn't always "pick the single most likely token" — settings
like temperature and top-p deliberately introduce randomness into which token gets
sampled from the distribution. The same prompt can produce different output on
different calls. Temperature near 0 makes output close to deterministic (always
picking the top candidate), but even then it isn't guaranteed to be byte-identical
across runs.

## Context windows

A context window is the maximum number of tokens a model can process in a single
call — input and output combined — and it's a hard ceiling, not a guideline. Exceed
it and the call either errors out or the API truncates the oldest tokens (often the
system prompt or earliest conversation turns). Two things follow directly for
OpsPilot: input and output tokens draw from the same shared budget, so a large prompt
leaves less room for a useful response; and nothing carries over between calls — each
API call is stateless, so a "conversation" only works because the app resends the
full prior history as context every time, up to the window limit. Sending more
history costs more tokens (money + latency), so how much lead/conversation context to
resend on each call is a real design tradeoff, not a free win.

## Hallucination

Models can generate confident, fluent, and completely incorrect information. This
happens because the model is optimized to produce plausible next tokens based on
patterns learned during training, not to verify claims against a source of truth — a
false but plausible-sounding continuation gets produced with the same fluency as a
correct one, with no internal signal distinguishing the two.

## Context vs. persistent knowledge

Context (what's in the prompt for a given call) is temporary — it exists only for
that call and is gone afterward. "Knowledge" from training is baked into the model's
weights at training time and can't be updated per-conversation or per-tenant. If
OpsPilot needs the model to work with a lead's history, that history must be
re-sent as context on every call; the model itself isn't storing anything about
past interactions.

## Why an LLM is not a database

A database returns exact, retrievable, auditable records — query it twice, get the
same answer, with a clear source. An LLM returns statistically likely text
reconstructed from training patterns, with no retrieval guarantee, no built-in
citation, and no consistency guarantee across calls. This is why OpsPilot's source of
truth for lead status/data is Postgres, never the model — the model only reasons over
data it's explicitly given in context, and its own output should never be treated as
a record of fact.

## Temperature and top-p

Both control how much randomness gets injected when picking the next token, but they
work differently. Temperature reshapes the whole probability distribution before
sampling: near 0, it sharpens the distribution so the model almost always picks the
top candidate (deterministic-feeling, conservative output); near 1+, it flattens the
distribution so lower-probability tokens get picked more often (more varied,
sometimes less coherent output). Top-p (nucleus sampling) works differently — instead
of reshaping probabilities, it restricts sampling to the smallest set of top tokens
whose cumulative probability reaches p (e.g. p=0.9 means only sample from the tokens
covering the top 90% of probability mass, ignoring the unlikely long tail). The two
are often used together. For OpsPilot, a low temperature (and/or low top-p) is the
right choice for anything that needs to be consistent and predictable — e.g. scoring
a lead the same way twice — while a higher temperature might be acceptable for
drafting varied follow-up email copy.

## Structured output

Left to itself, a model produces free-form text, which is unreliable to parse
programmatically (formatting drifts, fields get renamed, JSON comes back malformed).
Structured output constrains the model to return data in a fixed shape — usually JSON
matching a schema — either by prompting it strictly, using a provider's native
"JSON mode"/schema-constrained decoding, or validating and retrying on failure.
For OpsPilot, any place the model's output feeds directly into application logic
(e.g. a lead score, a suggested status change) must use structured output with
schema validation on the receiving end — never parse free text and hope the shape
holds.

## Nondeterminism and testing

Because sampling is probabilistic, the same prompt can produce different output on
different runs, which breaks the usual "assert exact output" style of testing. Tests
that call a real LLM need to assert on structural properties instead of exact
strings — e.g. "response is valid JSON matching the schema," "score is between 0 and
100," "required fields are present" — rather than "response equals this exact text."
For deterministic, repeatable tests, mock the LLM call entirely and test the
surrounding logic (parsing, validation, error handling) against fixed canned
responses; save real-LLM-call tests for a smaller, separate eval suite that tolerates
variation.

## Which application decisions must stay deterministic

Anything that is a business rule, a safety boundary, or affects money/access should
never be delegated to the model's probabilistic judgment — it should be plain
deterministic code. For OpsPilot specifically: tenant/franchisor access scoping,
whether a lead gets marked lost/closed, whether a message actually gets sent to a
customer, and any pricing/capacity calculation must all be deterministic application
logic that the model's output can only *suggest* into, never execute directly (this
lines up with the guardrails already in `README.md` — the AI recommends, a human or
deterministic rule enforces). The model is appropriate for judgment-y, low-stakes,
human-reviewed tasks: drafting a follow-up message, summarizing a lead's history,
suggesting (not applying) a priority score.

| OpsPilot decision                                  | LLM allowed?             | Why                                        |
| --------------------------------------------------- | ------------------------ | ------------------------------------------- |
| Summarize a lead                                   | Yes                      | Generative task                            |
| Draft follow-up                                    | Yes                      | Generative task                            |
| Recommend next action                              | Yes, bounded             | Must use approved choices                  |
| Calculate available capacity                       | **No**                   | Database calculation                       |
| Determine user's tenant access                     | **No**                   | Authorization rule                         |
| Decide whether franchisor admin can access tenant   | **No**                   | Security policy                            |
| Calculate price                                    | **No**                   | Business rule                              |
| Search policy documents                            | LLM may initiate         | Retrieval itself is deterministic tooling  |
| Send customer email                                | **No direct authority**  | Requires controlled action/approval        |
| Modify database record                             | **No direct authority**  | Tool + authorization + approval            |
| Score/prioritize a lead                            | Yes, bounded             | Suggestion only — human/deterministic rule confirms before it's stored as fact |
| Mark a lead lost/closed                            | **No**                   | Guardrail in `README.md` — requires human confirmation |
| Choose which tenant's data to query                | **No**                   | Tenant scope comes from the URL path, never model output |
| Validate request input                             | **No**                   | Trust boundary — Pydantic schemas, not the model |

