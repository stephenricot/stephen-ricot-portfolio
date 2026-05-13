from flask import Flask, render_template, request, jsonify
import datetime
import os

app = Flask(__name__)

# Home page – serves the portfolio HTML
@app.route('/')
def index():
    return render_template('index.html')

# Contact form endpoint (POST)
@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    message = data.get('message', '').strip()

    if not name or not email or not message:
        return jsonify({'success': False, 'error': 'All fields are required.'}), 400

    # Optional: simple email validation
    if '@' not in email or '.' not in email:
        return jsonify({'success': False, 'error': 'Invalid email address.'}), 400

    # Save the message to a text file (no database needed)
    with open('messages.txt', 'a', encoding='utf-8') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] From: {name} <{email}>\n{message}\n{'-'*40}\n")

    # In a real scenario you could also send an email using smtplib
    return jsonify({'success': True, 'message': 'Thank you! I will get back to you soon.'})

if __name__ == '__main__':
    app.run(debug=True)

port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=port)