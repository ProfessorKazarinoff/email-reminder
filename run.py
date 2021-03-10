# run.py

from datetime import datetime, timedelta
from pathlib import Path

from config import SENDGRID_API_KEY
from parse_roster import get_class_roster
from parse_schedule import create_message, get_instructor_dict, get_schedule_list
from sendgrid_email import send_sendgrid_email


def main():
    dt = datetime.now()
    schedule_json_fp = Path(Path.cwd(), "schedule.json")
    roster_csv_fp = Path(Path.cwd(), "roster.csv")
    schedule_list = get_schedule_list(schedule_json_fp)
    instructor_dict = get_instructor_dict(schedule_json_fp)
    class_roster_dict = get_class_roster(roster_csv_fp)
    class_email_list = class_roster_dict["student_email_list"]
    class_CRN = class_roster_dict["class_CRN"]
    for item in schedule_list:
        if class_CRN == item["CRN"]:
            reminder_email_content = create_message(
                item,
                date=f"{dt.strftime('%b')} {dt.strftime('%d')}",
                instructor_name=instructor_dict["first_name"],
            )
            print(reminder_email_content)
            send_sendgrid_email(
                from_email=instructor_dict["email"],
                to_email=class_email_list,
                subject=f'{item["class_name"]} {item["day"]} {dt.strftime("%b")} {dt.day} at {item["time"]}',
                content=reminder_email_content,
                API_KEY=SENDGRID_API_KEY,
            )


if __name__ == "__main__":
    main()
