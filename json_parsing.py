# json_parsing.py
"""
test module to parse out the meaningful parts of the json that contains the
dates you want to send reminders on
"""
import json

with open('example-schedule.json','r') as f:
    schedule = json.load(f)

print(schedule['reminders'][0].keys())
#['name', 'day', 'time', 'start_date', 'end_date', 'exclude_dates']
for item in schedule['reminders']:
    print(f"class name: {item['name']}")
    print(f"day: {item['day']}")
    print(f"time : {item['time']}")
    print()

"""
class name: ENGR114
day: Mon
time : 9:00am

class name: ENGR101
day: Mon
time : 1:00pm
"""
