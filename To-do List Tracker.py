#this program ask for data in a dictionary
#it can add,view, check the tasks if done, delete tasks, and exit the program manually
#for the basic Ill do the input taker, adder, and viewer.

"""
#Version 1
#intitialize the dictionary
TaskList = { }
numbers_Sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

Inputted_task = ""
while Inputted_task != "1":
    print("Press Enter to add the task, Press 1 to see your tasks.")
    Inputted_task = input("Input a task to do. ")
    TaskList[Inputted_task] = " not done"

del TaskList["1"]
print("These are your tasks: ")
Taskcount = len(TaskList) 

for i,(key,value) in zip(numbers_Sequence,TaskList.items()):
    print(f"{numbers_Sequence[i-1]}.{key}:{value}")

""" 
"""
#Version 2
#update: this one has a lot of bugs and wrong mechanics

#This program asks for the things the user will do, initially it initializes it as not done
#the user can add task, view all the tasks, mark as done, delete, and exit the program manually 

#Initializing the Dictionary
ToDoList = { }
num_sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

#getting the initial tasks
def get_task(ToDoList):
    user_input = ""
    while True:
        try:
            user_input = input("Input your tasks for Today. Press 1 if done: ")
            if user_input == "1":
                break
            ToDoList[user_input] = "Not Done"
        except Exception as e:
            print("Invalid Input. Enter a valid one.", e)

#adds the inputted task
def add_tasks(ToDoList):
    TaskToAdd = input("Input the task to add: ")
    ToDoList[TaskToAdd] = "Not Done"
    print(f"Task {TaskToAdd} added!")

#prints the tasks in ToDoList Dictionary  
def show_tasks(num_sequence):
    for (key,value),i in zip(ToDoList.items(),num_sequence):
        print(f"{num_sequence[i-1]}. {key} : '{value}'")

#prints the dictionary but has the decide menu at its end
def view_tasks(ToDoList):
    for (key,value),i in zip(ToDoList.items(),num_sequence):
        print(f"{num_sequence[i-1]}. {key} : '{value}'")

#marks the chosen task done
def taskMarker(ToDoList,show_tasks,add_tasks,taskMarker,taskDeleter,end_program):
    show_tasks(num_sequence)
    while True:
      try:    
        chosen_Task = input("What task to mark done?")
        ToDoList[chosen_Task] = "Done"
        print(f"{chosen_Task} marked Done.")
      except ValueError:
        print("Invalid Input. Please enter a valid one.")

#deletes the chosen task
def taskDeleter(ToDoList,add_tasks,show_tasks,taskMarker,taskDeleter,end_program):
    show_tasks(num_sequence)
    while True:
      try:
        chosenTask = input("What task do you wish to delete?")
        del ToDoList[chosenTask] #deleting the task
        print(f"{chosenTask} deleted.")
      except ValueError:
        print("Invalid Input. Please input a valid one.")
      
#ends the program
def end_program():
    print("Have a Good Day!")

#the main menu
def decide_menu(ToDoList,add_tasks,show_tasks,taskMarker,taskDeleter,end_program):
    choice_list = {"Add Task":1,"View Tasks":2,"Mark Task as done":3,"Delete Task":4, "Exit the program":5}
    print("What do you want to do? ")
    for key,value in choice_list.items():
        print (f"{key}? Press {value}")
    #choice loop
    while True:
        try:
            userChoice = int(input("Choose the number of your choice. "))
            
            if userChoice == 1:
                add_tasks(ToDoList,add_tasks,show_tasks,taskMarker,taskDeleter,end_program)
            elif userChoice == 2:
                view_tasks(ToDoList,add_tasks,show_tasks,taskMarker,taskDeleter,end_program)
            elif userChoice == 3:
                taskMarker(ToDoList,add_tasks,show_tasks,taskMarker,taskDeleter,end_program)
            elif userChoice == 4:
                taskDeleter(ToDoList,add_tasks,show_tasks,taskMarker,taskDeleter,end_program)
            elif userChoice == 5:
                end_program()
                break
        except ValueError:
            print("Invalid Input. Choose from the choices.")  

#main function
get_task(ToDoList)
decide_menu(ToDoList,add_tasks,show_tasks,taskMarker,taskDeleter,end_program)

"""

#byChatGPT

# Initializing the Dictionary
ToDoList = {}
num_sequence = list(range(1, 100))  # Supports up to 99 tasks

# Get initial tasks from user
def get_task(ToDoList):
    print("Input your tasks for Today. Type '1' when you're done.")
    while True:
        try:
            user_input = input("Task: ")
            if user_input == "1":
                break
            ToDoList[user_input] = "Not Done"
        except Exception as e:
            print("Invalid Input. Try again.", e)

# Add a new task
def add_tasks(ToDoList):
    TaskToAdd = input("Input the task to add: ")
    ToDoList[TaskToAdd] = "Not Done"
    print(f"Task '{TaskToAdd}' added!")

# Show all tasks with status
def show_tasks(ToDoList):
    if not ToDoList:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for (task, status), number in zip(ToDoList.items(), num_sequence):
            print(f"{number}. {task} : '{status}'")

# Mark a task as done
def taskMarker(ToDoList):
    show_tasks(ToDoList)
    task = input("Which task do you want to mark as done? Enter the exact task name: ")
    if task in ToDoList:
        ToDoList[task] = "Done"
        print(f"'{task}' marked as Done.")
    else:
        print("Task not found.")

# Delete a task
def taskDeleter(ToDoList):
    show_tasks(ToDoList)
    task = input("Which task do you want to delete? Enter the exact task name: ")
    if task in ToDoList:
        del ToDoList[task]
        print(f"'{task}' deleted.")
    else:
        print("Task not found.")

# Menu system
def decide_menu(ToDoList):
    while True:
        print("\nWhat do you want to do?")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit the Program")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_tasks(ToDoList)
            elif choice == 2:
                show_tasks(ToDoList)
            elif choice == 3:
                taskMarker(ToDoList)
            elif choice == 4:
                taskDeleter(ToDoList)
            elif choice == 5:
                print("Have a Good Day!")
                break
            else:
                print("Invalid choice. Please pick a number between 1–5.")
        except ValueError:
            print("Please enter a number (1–5).")

# --- Main Program Execution ---
get_task(ToDoList)
decide_menu(ToDoList)
