PrincessRuth90
/
alx-system_engineering-devops
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
alx-system_engineering-devops/0x15-api/1-export_to_CSV.py
@PrincessRuth90
PrincessRuth90 API Task
 1 contributor
Executable File  38 lines (33 sloc)  1.21 KB
#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
Export this data to CSV
"""
import csv
import requests
from sys import argv


def to_csv():
    """return API data"""
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in users.json():
        if u.get('id') == int(argv[1]):
            USERNAME = (u.get('username'))
            break
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    """export to csv"""
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    to_csv()
