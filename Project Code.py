import csv
import datetime

try:
    filename = 'task.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)

    timex = datetime.datetime.now()
    timeNow = f"{timex.month}/{timex.day}/{timex.year}"

    def addTask():
        name = input("Please enter the name for your task: ")
        category = input("Enter a category for the task (ex. FA, AA, SA): ")
        deadline = input("Enter the deadline in this format, MM/DD/YYYY: ")
        notes = input("Enter the notes for the task: ")
        status = False
        if status == False:
            print("Task is not finished.")
        else:
            print("Task is finished!")

        if deadline < timeNow:
            task_overdue = True
        else:
            task_overdue = False

        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, category, deadline, notes, task_overdue, status ])
        print("Done!")

    def editTask():
        TaskChoice = input("Please enter the name of the task you want to edit: ")
        for name in filename:
            if name["Task Name"] == TaskChoice:
                name["Finished?"] = True


    choice = 0
    print("\nWelcome to our Smart Study Planner!")
    print(f"Today's date is {timex.month}/{timex.day}/{timex.year}")
    while choice != 5:
        choice = int(input("\nPlease pick an option.\n1. View Instructions\n2. Add a task.\n3. Edit a task\n4. Delete a task\n5. Exit\n(Currently, viewing instructions and adding a task is the only option available.)\n\nInput your choice here: "))
        if choice == 1:
            print(4*"*","INSTRUCTIONS",4*"*")
            print("\nWhat does our code do?\nThis code's purpose is to help students on their studies by tracking their tasks.\nStudents can add a task, edit a task, or delete a task in this code. ")
            print("\nWhat does each menu option do?\nFirstly, choosing 2 will add a task, the code will then ask the user to input the name, category, deadline, and notes for your task.\nSecondly, pressing 3 will edit a task, which will ask the user what task and part of it to be edited.\nThird, pressing 4 will ask a player what task to delete and if they want to confirm it.\nLastly, pressing 5 will end the program.")
        elif choice == 2:
            addTask()
        elif choice == 3:
            editTask()
        elif choice == 4:
            print("\nSorry, this option is not yet available. Please pick option 1, 2 or exit.")
        else:
            print("\nWrong input, please pick from 1-4.")


except FileNotFoundError:
    print("Failed to open the file.")