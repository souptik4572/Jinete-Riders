from django.http import JsonResponse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from decouple import config

from decouple import config
sendgrid_key = config("SENDGRID_API_KEY")
PASSWORD_RESET_EMAIL_TEMPLATE_ID = config('PASSWORD_RESET_EMAIL_TEMPLATE_ID')


def send_password_reset_email(data):
    reset_password_link = f"jinete.com/passwordReset?token={data['token']}&id={data['id']}"
    message = Mail(from_email='yunoasta6602@gmail.com',
                   to_emails=[data['receiver']])
    message.dynamic_template_data = {
        'reset_password_url': reset_password_link
    }
    message.template_id = PASSWORD_RESET_EMAIL_TEMPLATE_ID
    try:
        sg = SendGridAPIClient(api_key=sendgrid_key)
        sg.send(message)
    except Exception as e:
        JsonResponse({
            'success': False,
            'message': str(e)
        })
