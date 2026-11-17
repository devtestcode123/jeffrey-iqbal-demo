# Jeffrey Iqbal — Website

A one-page static site for Jeffrey Iqbal. Currently it's a client demo on GitHub Pages; later it becomes the final .com.

## Layout

```
index.html            the whole site (one page, section anchors)
assets/css/style.css  all styles
assets/js/main.js     scroll reveal, pixel equalizer, booking form
assets/img/           photos (see below)
backend/              optional Flask endpoint that emails booking enquiries
scripts/scraper.py    one-off tool that pulled text from the old jeffreyiqbal.com
docs/                 design references
```

## Photos

`assets/img/` holds six photos (`hero`, `live`, `stage`, `crowd`, `studio`, `candid`) and three covers (`cover-*.jpg`). They're 1280×720 stills and title cards taken from Jeffrey's own YouTube music videos. Swap in proper photography from the client for the .com, keeping the same file names (they're case-sensitive on GitHub Pages). The page displays them in black and white. A missing photo shows as a dark panel.

## Music links

- Spotify artist: `0QJN3RYr6xAyScRqhkephw`
- Apple Music artist: `561702291`
- YouTube channel: `@jeffreyiqbal`, which the uploads playlist embed reads from

The players in the Listen section load only when scrolled near. YouTube Music has no embeddable player, so it's a link button.

## Run locally

```powershell
python -m http.server 8000   # then open http://localhost:8000
```

## Deploy the demo (GitHub Pages)

Push to GitHub → Settings → Pages → Deploy from branch → `main` / root.
GitHub Pages can't run the backend, so the booking form opens the visitor's email app with the enquiry already filled in.

## Booking backend (for the final .com)

The form POSTs `{name, email, subject, message}` to `/api/contact`. The backend has to be served from the same domain as the site, e.g. behind a reverse proxy.

```powershell
python -m venv .venv; .\.venv\Scripts\activate
pip install -r backend/requirements.txt
copy backend\.env.example backend\.env   # set SMTP_HOST, SMTP_USER, SMTP_PASSWORD, ADMIN_EMAIL
python backend/app.py
```

Without SMTP settings, the backend writes the last enquiry to `data/last_email.json` instead of sending it.

## Before launching the .com

- Remove the `noindex` meta tag at the top of `index.html`.
- Host the backend, or switch the form to a form service.
