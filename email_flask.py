from flask import Flask, request, jsonify
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

APP = Flask(__name__)

@APP.route('/sendemail', methods=['GET'])
def sendemail():
 message = Mail(
    from_email='from_email@example.com',
    to_emails='saurabh.gupta2@tatacommunications.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
 try:
    #sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return "Email Sent- Test Email for NPIU"

 except Exception as e:
    print(e.message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
