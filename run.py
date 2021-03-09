# run.py

from pathlib import Path
from datetime import datetime

from schedule_parse import create_message, get_schedule_list, get_instructor_first_name
from sendgrid_email import send_sendgrid_email

from config import SENDGRID_API_KEY

def main():
    dt = datetime.now()
    schedule_json_fp = Path(Path.cwd(),'schedule.json')
    schedule_list = get_schedule_list(schedule_json_fp)
    instructor_first_name = get_instructor_first_name(schedule_json_fp)
    for item in schedule_list:
        if True:
            reminder_email_content = create_message(
                item,
                date='Feb 3',
                link='https:zoom.us',
                instructor_name=instructor_first_name)
            send_sendgrid_email(
                from_email='peter.kazarinoff',
                to_email="ENGR114",
                subject="ENGR114 Fri Mar 3 at 9am",
                content = reminder_email_content,
                API_KEY=SENDGRID_API_KEY
            )

if __name__ == "__main__":
    main()