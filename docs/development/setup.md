# Votera — Development Setup

## Prerequisites

Install:
- Git
- Node.js
- npm
- Python
- pip
- Supabase project

## Frontend

```bash
cd frontend
npm install
npm run dev
```

The Vite development server is expected to run on the configured local port.

## Backend

```bash
cd backend
python -m venv venv
```

Activate the virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn app.main:app --reload
```

## Environment Variables

Backend configuration should be stored in `.env`.

Expected categories include:

```text
SUPABASE_URL
SUPABASE_KEY
RESEND_API_KEY
PAYSTACK_SECRET_KEY
HUBTEL_CLIENT_ID
HUBTEL_CLIENT_SECRET
```

Do not commit `.env`.

## Local Development

Frontend should call the local FastAPI API.

Production URLs must never be hard-coded into development code.
