import csv
import datetime

try:
    with open('task.csv', 'r') as file:
        reader = csv.reader(file)

    with open('task.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Task Name', 'Category', 'Deadline', 'Notes', 'Overdue?', 'Finished?'])


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
    while choice != 4:
        choice = int(input("\nWelcome to our Smart Study Planner! \n \nPlease pick an option. \n1.Add a task.\n2.Edit a task\n3. Delete a task\n4. Exit\n(Currently, adding a task is the only option available.)\n\nInput your choice here: "))
        if choice == 1:
            addTask()
        elif choice == 2:
            print("\nSorry, this option is not yet available. Please pick option 1 (Add a task) or exit.")
        elif choice == 3:
            print("\nSorry, this option is not yet available. Please pick option 1 (Add a task) or exit.")
        else:
            print("\nWrong input, please pick from 1-4.")


except FileNotFoundError:
    print("Failed to open the file.")