# schedule_parse.py

import json


def get_schedule_list(schedule_json_file_path=None):
    with open(schedule_json_file_path, "r") as f:
        schedule_dict = json.load(f)
    return schedule_dict["courses"]


def get_instructor_dict(schedule_json_file_path=None):
    with open(schedule_json_file_path, "r") as f:
        schedule_dict = json.load(f)
    return schedule_dict["instructor"]


def create_message(class_dict, date="", instructor_name=""):
    return f"""Hello {class_dict['class_name']},
    
    This is a reminder that we have class today, {class_dict['day']}, {date} at {class_dict['time']}. Zoom link below:
    
    {class_dict["zoom_link"]}

    See you soon,
    {instructor_name}"""
