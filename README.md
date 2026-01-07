# Flashy FastAPI: Czech History (One Paragraph)

Pink, neon-styled FastAPI single-page app that serves a one-paragraph overview of Czech history at the root endpoint.

## Quick start
- Python 3.10+ recommended.
- (Optional) create a virtual env: `python -m venv .venv && source .venv/bin/activate`
- Install deps: `pip install -r requirements.txt`
- Run dev server: `uvicorn main:app --reload --host 0.0.0.0 --port 8000`

## What you get
- `GET /` returns a vivid HTML page with a concise Czech Republic history blurb.
- Inline CSS delivers the “very pink and flashy” look—no extra assets required.

## Files
- `main.py` — FastAPI app and HTML response.
- `requirements.txt` — Minimal runtime dependencies.

## Notes
- Intended for quick demo/showcase; static content is inlined for simplicity.
