# sendgrid_email.py

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from config import SENDGRID_API_KEY, FROM_EMAIL, TO_EMAIL

message = Mail(
    from_email=FROM_EMAIL,
    to_emails=TO_EMAIL,
    subject='Subject for a test email',
    html_content="""This is a reminder:\n\n
    Remember to do that thing.
    """
    )

def main():
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

if __name__ == "__main__":
    main()
