# Problem Brief — OpsPilot

**Date:** 2026-07-16  
**Workflow:** Lead Handling (Preschool Admissions)

---

## Users

- **Founder + Business Partner** — receive and initially log incoming leads
- **Preschool Admin Team** — own follow-up and lead nurturing after entry

---

## Current Process (Step-by-Step)

1. Lead arrives via one of multiple channels: Facebook Ads, Instagram Ads, Google Ads, WhatsApp/phone inquiry, website form, walk-in, or referral
2. Founder or business partner receives or spots the lead
3. Lead details manually entered into a Google Sheet
4. Entry is made ad hoc — no standard timing or format enforced
5. Admin team reviews the sheet (no automated notification)
6. Admin team calls or messages the lead to follow up
7. Notes from the call are (sometimes) added back to the sheet
8. If no response, follow-up may or may not happen again
9. Lead status updated manually if someone remembers
10. No clear handoff point between "active" and "cold" leads
11. Decisions on dropping or escalating a lead are made informally
12. No reporting on conversion rate, source quality, or time-to-contact

---

## Pain Points

- **Leads fall through the cracks** — high inbound volume + manual process = missed leads
- **No visibility on lead status** — founder and admin team have no shared real-time picture
- **Inconsistent follow-up timing** — some leads get contacted within hours, others wait days
- **GSheet entry is error-prone** — duplicates, missing fields, inconsistent formatting
- **No source attribution** — unknown which ad channels produce quality leads
- **Repeated manual work** — copy-paste from DMs/forms into sheet, follow-up reminders set by hand

---

## Actions the AI Should Recommend

1. **Score and rank leads** — based on source, response time, and engagement signals
2. **Draft follow-up message** — suggest a WhatsApp or email reply tailored to the lead's inquiry
3. **Flag stale leads** — surface any lead with no activity in > 48 hours and suggest a next step
4. **Suggest action** - whether to call, message, or deprioritize based on lead signals

---

## Actions the AI Must Never Execute Without Approval

1. **Send any message or email** — all outbound communication requires human review and sign-off
2. **Mark a lead as lost or closed** — no status changes without explicit confirmation
3. **Share lead data externally** — no PII sent to third-party services, APIs, or tools without approval

---

## Open Questions

- Where does the GSheet live and who has edit access?
- Is there a CRM in use or planned, or is GSheet the long-term source of truth?
- What is the target time-to-first-contact (e.g., under 1 hour)?
- Are WhatsApp messages the primary follow-up channel or phone calls?

---

## Discovery Questions

1. When a lead comes in and nothing goes wrong — what does the ideal end-to-end experience look like for both the family and your team?
2. Think of a lead you lost that you shouldn't have — what happened, and at what point did it go wrong?
3. How do you currently decide whether a lead is worth pursuing or not, and how confident are you in that judgment?
4. What information about a lead do you wish you had at the moment of first contact that you usually don't?
5. When a lead goes cold after initial contact, what does your team do today — and what do you wish they did?
6. How do you know, right now, how many active leads are in the pipeline and what stage each one is at?
7. Which ad channel or source do you believe brings the best-quality leads, and what makes you think that?
8. If you had to hand this entire workflow to someone new tomorrow, what would be the three things most likely to break?
9. What does a "won" lead look like — what's the moment you consider it converted, and who records that?
10. If the admin team could spend less time on one repetitive task in this workflow, what would they say it is?
