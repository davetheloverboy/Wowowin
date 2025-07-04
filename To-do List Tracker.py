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

#Version 2

#This program asks for the things the user will do, initially it initializes it as not done
#the user can add task, view all the tasks, mark as done, delete, and exit the program manually 

#Initializing the Dictionaty
ToDoList = { }
num_sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

#getting the initial tasks
def get_task(ToDoList,add_tasks,print_dict,taskMarker,taskDeleter,end_program):
    user_input = ""
    while user_input != "1":
        user_input = input("Input your tasks for Today. Press 1 if done: ")
        ToDoList[user_input] = "Not Done"
    del ToDoList["1"]
    decide_menu(add_tasks,print_dict,taskMarker,taskDeleter,end_program)

def add_tasks(ToDoList,add_tasks,print_dict,taskMarker,taskDeleter,end_program):
    TaskToAdd = input("Input the task to add: ")
    ToDoList[TaskToAdd] = "Not Done"
    print(f"Task {TaskToAdd} added!")
    decide_menu(add_tasks,print_dict,taskMarker,taskDeleter,end_program)

#prints the tasks in ToDoList Dictionary  
def print_dict(ToDoList):
    for (key,value),i in zip(ToDoList.items(),num_sequence):
        print(f"{num_sequence[i-1]}. {key} : '{value}'")

def view_tasks(ToDoList,add_tasks,print_dict,taskMarker,taskDeleter,end_program):
    for (key,value),i in zip(ToDoList.items(),num_sequence):
        print(f"{num_sequence[i-1]}. {key} : '{value}'")
    decide_menu(add_tasks,print_dict,taskMarker,taskDeleter,end_program)

def taskMarker(ToDoList,print_dict,add_tasks,taskMarker,taskDeleter,end_program):
    print_dict(ToDoList)
    chosen_Task = input("What task to mark done?")
    ToDoList[chosen_Task] = "Done"
    decide_menu(add_tasks,print_dict,taskMarker,taskDeleter,end_program)
                        
def taskDeleter(ToDoList,add_tasks,print_dict,taskMarker,taskDeleter,end_program):
    print_dict(ToDoList)
    chosenTask = input("What task do you wish to delete?")
    del ToDoList[chosenTask] #deleting the task
    decide_menu(add_tasks,print_dict,taskMarker,taskDeleter,end_program)
    
def end_program():
    print("Have a Good Day!")

def decide_menu(add_tasks,print_dict,taskMarker,taskDeleter,end_program):
    choice_list = {"Add Task":1,"View Tasks":2,"Mark Task as done":3,"Delete Task":4, "Exit the program":5}
    print("What do you want to do? ")
    for key,value in choice_list.items():
        print (f"{key}? Press {value}")
    #choice loop
    userChoice = int(input("Choose the number of your choice. "))
    while True:
        try:
            if userChoice == 1:
                add_tasks(ToDoList,add_tasks,print_dict,taskMarker,taskDeleter,end_program)
            elif userChoice == 2:
                view_tasks(ToDoList,add_tasks,print_dict,taskMarker,taskDeleter,end_program)
            elif userChoice == 3:
                taskMarker(ToDoList,add_tasks,print_dict,taskMarker,taskDeleter,end_program)
            elif userChoice == 4:
                taskDeleter(ToDoList,add_tasks,print_dict,taskMarker,taskDeleter,end_program)
            elif userChoice == 5:
                end_program()
            break
        except ValueError:
            print("Invalid Input. Choose from the choices.")  
        break  

get_task(ToDoList,add_tasks,print_dict,taskMarker,taskDeleter,end_program)
decide_menu(add_tasks,print_dict,taskMarker,taskDeleter,end_program,)




