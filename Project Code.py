import csv
import datetime

try:
    with open('task.csv', 'r') as file:
        reader = csv.reader(file)

    def addTask():
        name = input("Please enter the name for your task: ")
        category = input("Enter a category for the task (ex. FA, AA, SA): ")
        deadline = input("Enter the deadline in this format: MM/DD/YYYY. ")
        notes = input("Enter the notes for the task: ")
        with open('task.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, category, deadline, notes])
        print("Done!")
        print("Here are the tasks.")
        with open('task.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                for item in row:
                    print(item)

    choice = 0
    while choice != 5:
        choice = int(input("\nWelcome to our Smart Study Planner! \n \nPlease pick an option.\n1. View Instructions\n2. Add a task.\n3. Edit a task\n4. Delete a task\n4. Exit\n(Currently, viewing instructions and adding a task is the only option available.)\n\nInput your choice here: "))
        if choice == 1:
            print(4*"*","INSTRUCTIONS",4*"*")
            print("\nWhat does our code do?\nThis code's purpose is to help students on their studies by tracking their tasks.\nStudents can add a task, edit a task, or delete a task in this code. ")
            print("\nWhat does each menu option do?\nFirstly, choosing 2 will add a task, the code will then ask the user to input the name, category, deadline, and notes for your task.\nSecondly, pressing 3 will edit a task, which will ask the user what task and part of it to be edited.\nThird, pressing 4 will ask a player what task to delete and if they want to confirm it.\nLastly, pressing 5 will end the program.")
        elif choice == 2:
            addTask()
        elif choice == 3:
            print("\nSorry, this option is not yet available. Please pick option 1, 2 or exit.")
        elif choice == 4:
            print("\nSorry, this option is not yet available. Please pick option 1, 2 or exit.")
        else:
            print("\nWrong input, please pick from 1-4.")


except FileNotFoundError:
    print("Failed to open the file.")