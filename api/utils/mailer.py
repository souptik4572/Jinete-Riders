from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from decouple import config

import sendgrid
from decouple import config
sendgrid_key = config("SENDGRID_API_KEY")


def send_email(to_email, subject, value):
    send_grid = sendgrid.SendGridAPIClient(api_key=sendgrid_key)
    data = get_data(to_email, subject, value)
    send_grid.send(data)


def get_data(to_email, subject, value):
    return {
        "personalizations": [{"to": [{"email": to_email}], "subject":
                             subject}],
        "from": {"email": "yunoasta6602@gmail.com", "name": "My Company"},
        "content": [{"type": "text/html", "value": value}],
    }

send_email("souptiksarkar4572@gmail.com", "Hello World!", "<p>Welcome,valued customer!</p>")