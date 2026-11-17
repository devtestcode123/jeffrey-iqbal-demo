import os
import sys
from html import escape
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent / '.env')

sys.path.insert(0, str(Path(__file__).parent))
from email_utils import send_email_smtp

SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'info@jeffreyiqbal.com')
FROM_EMAIL = os.getenv('FROM_EMAIL', ADMIN_EMAIL)

app = Flask(__name__)
CORS(app)


@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')
    subject_text = data.get('subject', 'New website contact')
    message = data.get('message', '')
    if not name or not email or not subject_text:
        return jsonify({'error': 'name, email, and subject required'}), 400

    subject = f'Website contact: {subject_text} — {name} <{email}>'
    esc = lambda v: escape(str(v))  # visitor input must not inject markup into the admin's inbox
    html = (
        f"<p><strong>Name:</strong> {esc(name)}</p>"
        f"<p><strong>Email:</strong> {esc(email)}</p>"
        f"<p><strong>Subject:</strong> {esc(subject_text)}</p>"
        f"<p><strong>Message:</strong><br>{esc(message)}</p>"
    )

    try:
        if SMTP_HOST:
            send_email_smtp(SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, subject, html, [ADMIN_EMAIL], FROM_EMAIL)
            return jsonify({'ok': True})
        else:
            # fallback: write to file
            out = {'subject': subject, 'to': ADMIN_EMAIL, 'html': html}
            path = Path(__file__).resolve().parents[1] / 'data' / 'last_email.json'
            path.parent.mkdir(parents=True, exist_ok=True)
            import json

            with open(path, 'w', encoding='utf-8') as f:
                json.dump(out, f, indent=2)
            return jsonify({'ok': True, 'note': 'no SMTP configured; wrote to data/last_email.json'})
    except Exception as e:
        app.logger.exception('send failed')
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
