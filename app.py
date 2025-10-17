import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Email Configuration from environment variables
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SENDER_EMAIL = os.getenv('student.community.habesha@gmail.com')
SENDER_PASSWORD = os.getenv('@Biniam235')
RECEIVER_EMAIL = 'bestenoughproperty@gmail.com' # The email provided by the user

def send_booking_email(data):
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("Error: student.community.habesha@gmail.com or @Biniam235 not set in .env file.")
        return False

    # Construct the email content
    subject = "New Booking Request from Website"
    body = f"""
    A new booking request has been submitted:

    Name: {data.get('name', 'N/A')}
    Email: {data.get('email', 'N/A')}
    Phone: {data.get('phone', 'N/A')}
    Check-in Date: {data.get('checkin', 'N/A')}
    Check-out Date: {data.get('checkout', 'N/A')}
    Guests: {data.get('guests', 'N/A')}
    Message: {data.get('message', 'N/A')}
    """

    msg = MIMEMultipart()
    msg['From'] = student.community.habesha@gmail.com
    msg['To'] = @Biniam235
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Use TLS encryption
            server.login(student.community.habesha@gmail.com, @Biniam235)
            server.sendmail(student.community.habesha@gmail.com, bestenoughproperty@gmail.com, msg.as_string())
        print(f"Email successfully sent to {bestenoughproperty@gmail.com}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    # Get form data from the request
    data = request.form.to_dict()
    
    # Simple validation (can be expanded)
    if not data.get('name') or not data.get('email') or not data.get('checkin'):
        return jsonify({'success': False, 'message': 'Missing required fields.'}), 400

    # Send the email
    if send_booking_email(data):
        return jsonify({'success': True, 'message': 'Booking request received and email sent successfully.'}), 200
    else:
        return jsonify({'success': False, 'message': 'Booking request received but failed to send email. Please check server logs.'}), 500

if __name__ == '__main__':
    # Running on a different port (e.g., 5000) than a typical web server (80/443)
    # The user will need to run this script.
    app.run(host='0.0.0.0', port=5000)
