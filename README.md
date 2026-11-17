# Jeffrey Iqbal — Site (Static)

This workspace includes a root-level static website with original homepage styling and simple page navigation. The site is built for easy hosting on GitHub Pages, Netlify, Vercel, or any static server.

Quick GitHub Pages deploy:

1. Create a GitHub repo and push this project.
2. In the repository settings enable GitHub Pages and set the site source to the `main` branch and root folder.
3. Your site will be available at `https://<username>.github.io/<repo>/`.

Alternatively, deploy the repository root to Netlify or Vercel and serve the pages directly.

Notes:
- The contact page uses JavaScript to POST to `/api/contact` when a backend is running.
- If you host the site as static-only, the contact form will still render but will show a fallback message.
- Spotify, YouTube, and Apple Music links are included and open in new tabs.

Project layout
------------

- Root HTML pages: `index.html`, `about.html`, `music.html`, `packages.html`, `video.html`, `contact.html`.
- `assets/`: static assets and shared CSS. Use `assets/css/style.css` for page styling.
- `scripts/`: developer scripts and optional backend.
- `scripts/backend/`: Flask contact endpoint and SMTP email utility.
- `data/`: runtime data and debug artifacts (`last_email.json` when SMTP is not configured).
- `docs/`: design notes and references.

Run local preview: open `index.html` in a browser or serve with a simple static server, e.g.:

```powershell
# from workspace root
python -m http.server 8000
# then open http://localhost:8000
```

Backend (optional) — to send contact form emails to Jeffrey's email:

1. Copy `scripts/backend/.env.example` to `scripts/backend/.env` and set `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, and `ADMIN_EMAIL` (default is `info@jeffreyiqbal.com`).
2. Install backend deps and run:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r scripts/backend/requirements.txt
python scripts/backend/app.py
```

3. With the backend running, open `http://localhost:5000/contact.html` in a browser and submit the form — the server will email the submission to `ADMIN_EMAIL`.

If SMTP is not configured, the backend saves the last submission to `data/last_email.json` for review.
