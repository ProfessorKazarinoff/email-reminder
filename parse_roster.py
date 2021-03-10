# parse_roster.py

import csv
from pathlib import Path


def get_class_roster(roster_file_path=None):
    d = {"class_CRN": "", "student_email_list": []}
    with open(roster_file_path, "r") as f:
        reader = csv.reader(
            f,
            delimiter=",",
        )
        next(reader)
        for row in reader:
            d["class_CRN"] = str(row[1])
            d["student_email_list"].append(row[6])
    return d


"""
{'class_CRN':'234432','student_email_list':['email1@college.edu', 'email2@college.edu']}
"""


def main():
    fp = Path(Path.cwd(), "example-roster.csv")
    d = get_class_roster(fp)
    print(d)


if __name__ == "__main__":
    main()
