
#THIS IS ONLY TO TEST SENDGRID ! THIS FILE WILL BE DELETED !

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='pasiekaradosc@gmail.com',
    to_emails='tomekklewicki@gmail.com',
    subject='The NEWEST - Sendgrid EMAIL for you',
    html_content='<strong>HEY HEY new emial for you, even with Python</strong>')
try:

    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
