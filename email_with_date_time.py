# email_with_date_time.py

import datetime

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from config import FROM_EMAIL, SENDGRID_API_KEY, TO_EMAIL, ZOOM_LINK

d = datetime.datetime.now()
d_of_week = d.strftime("%A")
month = d.strftime("%B")
day = d.strftime("%d")
start_time = "9:00am"
zoom_link = ZOOM_LINK

message = Mail(
    from_email=FROM_EMAIL,
    to_emails=TO_EMAIL,
    subject="Subject for a test email",
    html_content=f"""This is a reminder:\n\n
    Remember to do that thing, today {d_of_week}, {month}, {day} at {start_time}. Zoom link below:\n\n
    <a href={ZOOM_LINK}>{ZOOM_LINK}</a>
    
    """,
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
