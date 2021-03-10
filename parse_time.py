# parse_time.py

from datetime import timedelta


def hour_from_dt(dt=None):
    return dt.strftime("%I").lstrip("0") + ":00" + dt.strftime("%p").lower()


def is_hour_before_class(dt=None, class_dict={}):
    dt_plus_hour = dt + timedelta(hours=1)
    if class_dict["time"] == hour_from_dt(dt_plus_hour):
        return True
    else:
        return False


def is_day_of_class(dt=None, class_dict={}):
    if class_dict["day"] == dt.strftime("%b"):
        return True
    else:
        return False


def is_vacation_day(dt=None, schedule_dict={}):
    # if it is one of the days that is a vacation day, return True
    # if it isn't a vacation day, return False
    pass


def is_in_term(dt=None, schedule_dict={}):
    # if today is between the start of the term and the end of the term, return True
    pass


def send_reminder(dt=None, schedule_dict={}, class_dict={}):
    if (
        is_in_term(dt, schedule_dict)
        and not is_vacation_day(dt, schedule_dict)
        and is_day_of_class(dt, class_dict)
        and is_hour_before_class(dt, class_dict)
    ):
        return True
    else:
        return False
