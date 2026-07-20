# GCP Setup

## Project

| Key | Value |
|-----|-------|
| **Project ID** | `deft-observer-131923` |
| **Project Number** | `642095020119` |
| **Region** | `us-central1` |
| **Zone** | `us-central1-a` |

## Naming Conventions

| Resource | Pattern | Example |
|----------|---------|---------|
| Service accounts | `opspilot-<role>-sa` | `opspilot-sheets-sa` |
| Cloud Run services | `opspilot-<service>` | `opspilot-backend` |
| Storage buckets | `opspilot-<purpose>-<env>` | `opspilot-evals-prod` |
| Secret Manager secrets | `opspilot-<name>` | `opspilot-anthropic-key` |
| Pub/Sub topics | `opspilot-<event>` | `opspilot-lead-received` |

All resources use lowercase + hyphens. No underscores. No abbreviations beyond `sa` (service account).

---

## Auth

```bash
gcloud auth login
gcloud auth application-default login
gcloud config set project deft-observer-131923
gcloud config set compute/region us-central1
```

## Services to Enable

```bash
gcloud services enable sheets.googleapis.com
gcloud services enable drive.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable secretmanager.googleapis.com
```

## Service Account (for Google Sheets access)

```bash
gcloud iam service-accounts create opspilot-sheets-sa \
  --display-name="OpsPilot Sheets Service Account"

gcloud iam service-accounts keys create credentials.json \
  --iam-account=opspilot-sheets-sa@deft-observer-131923.iam.gserviceaccount.com
```

> Add `credentials.json` to `.gitignore` — never commit it.
