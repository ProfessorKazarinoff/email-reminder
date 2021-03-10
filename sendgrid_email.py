# sendgrid_email.py

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from config import SENDGRID_API_KEY


def send_sendgrid_email(from_email="", to_email="", subject="", content="", API_KEY=""):
    message = Mail(
        from_email=from_email, to_emails=to_email, subject=subject, html_content=content
    )
    try:
        sg = SendGridAPIClient(API_KEY)
        response = sg.send(message)
        return {
            "status_code": response.status_code,
            "body": response.body,
            "headers": response.headers,
        }
    except Exception as e:
        return {"message": e}


def main():
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject="Subject for a test email",
        html_content="""This is a reminder:\n\n
    Remember to do that thing.
    """,
    )
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
