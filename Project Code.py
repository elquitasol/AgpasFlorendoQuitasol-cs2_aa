import csv
import os
import datetime
from time import sleep

filename = 'task.csv'

# Get current date
timex = datetime.datetime.now()
timeNow = datetime.datetime(timex.year, timex.month, timex.day)

# Ensure file exists with headers
if not os.path.exists(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
    writer.writerow(['Task Name', 'Category', 'Deadline', 'Notes', 'Overdue?', 'Finished?'])

def addTask():
    name = input("Please enter the name for your task: ")
    category = input("Enter a category for the task (ex. FA, AA, SA): ")
    deadline_input = input("Enter the deadline in this format, MM/DD/YYYY: ")
    notes = input("Enter the notes for the task: ")

    status = False

    if status == False:
        print("Task is not finished.")
    else:
        print("Task is finished!")

    # Convert deadline to datetime
    deadline = datetime.datetime.strptime(deadline_input, "%m/%d/%Y")

    # Check overdue properly
    if deadline < timeNow:
        task_overdue = True
    else:
        task_overdue = False

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, category, deadline_input, notes, task_overdue, status])

    print("Done!")
    sleep(2)


def editTask():
    task_name = input("Enter the task name you want to edit: ")

    rows = []
    found = False

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for r in reader:
            if r['Task Name'] == task_name:
                found = True
    print("Task found. Leave blank if you don’t want to change something.")

    new_name = input(f"New name ({r['Task Name']}): ") or r['Task Name']
    new_category = input(f"New category ({r['Category']}): ") or r['Category']
    new_deadline = input(f"New deadline ({r['Deadline']}): ") or r['Deadline']
    new_notes = input(f"New notes ({r['Notes']}): ") or r['Notes']

    finished_input = input("Is it finished? (yes/no): ").lower()
    if finished_input == "yes":
        status = True
    elif finished_input == "no":
        status = False
    else:
        status = r['Finished?'] == 'True'

    # Recompute overdue
    deadline_dt = datetime.datetime.strptime(new_deadline, "%m/%d/%Y")
    task_overdue = deadline_dt < timeNow

    r = {
        'Task Name': new_name,
        'Category': new_category,
        'Deadline': new_deadline,
        'Notes': new_notes,
        'Overdue?': task_overdue,
        'Finished?': status
        }

    rows.append(r)

    if not found:
        print("Task not found.")
        return

    with open(filename, 'w', newline='') as file:
        fieldnames = ['Task Name', 'Category', 'Deadline', 'Notes', 'Overdue?', 'Finished?']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Task updated!")


def deleteTask():
    task_name = input("Please enter the name of the task you want to delete: ")

    rows = []
    found = False

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for r in reader:
            if r['Task Name'] != task_name:
                rows.append(r)
        else:
            found = True

    if not found:
        print("Task not found.")
        return

    confirm = input("Are you sure you want to delete this task? (yes/no): ").lower()
    if confirm != "yes":
        print("Deletion cancelled.")
        return

    with open(filename, 'w', newline='') as file:
        fieldnames = ['Task Name', 'Category', 'Deadline', 'Notes', 'Overdue?', 'Finished?']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Task deleted!")


choice = 0
print("\nWelcome to our Smart Study Planner!")
sleep(1)
print(f"Today's date is {timex.month}/{timex.day}/{timex.year}")
sleep(1)

while choice != 5:
    choice = int(input("\nPlease pick an option.\n1. View Instructions\n2. Add a task.\n3. Edit a task\n4. Delete a task\n5. Exit\n\nInput your choice here: "))

    if choice == 1:
        print(4*"*","INSTRUCTIONS",4*"*")
        sleep(2)
        print("\nThis program helps track study tasks.")
        sleep(1)
        print("\n2 = Add | 3 = Edit | 4 = Delete | 5 = Exit")
        sleep(3)
        input("\nPress enter to go back.")

    elif choice == 2:
        addTask()

    elif choice == 3:
        editTask()

    elif choice == 4:
        deleteTask()

    elif choice == 5:
        print("\nThank you for using our code!")
        exit(0)

    else:
        print("\nWrong input, please pick from 1-5.")