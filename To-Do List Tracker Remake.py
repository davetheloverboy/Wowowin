#the first one it had bugs that i couldn't fix, I will ask ai for help. 
#Then make another one from my own understanding/knowledge from the past program. 
#This program asks for tasks from the user to input in the dictionary.
#The user can add, view, mark as done, or delete the tasks, and the user can also end the program.

#Initializing the Dictionary
List_of_Tasks = { }
#makes a list ranging form 1-50
NumberList = list(range(1,50))

#primarily gets the list of tasks and puts it into the dictionary. 
def task_getter(List_of_Tasks):
    print("What are your tasks for today? Input 1 to stop")
    while True:
        try:
            userInput = input("Task: ")
            if userInput == "1":
                break
            List_of_Tasks[userInput] = "Not Done."
        except ValueError:
            print("Invalid Input.")

#adds tasks based on user input
def task_adder(List_of_Tasks):
    while True:
        try:
            userInput = input("What task do you want to add?: ")
            if userInput in List_of_Tasks:
                print(f"'{userInput} already in the List.")
            else:
                print(f"'{userInput}' has been added.")
                List_of_Tasks[userInput] = "Not Done."
                break
        except ValueError:
            print("Invalid Input.")

#prints the current tasks 
def task_viewer(List_of_Tasks):
    print("These are your current tasks:")
    for index,(key,value) in enumerate(List_of_Tasks.items(),1):
        print(f"{index}. {key} : {value}")

#deletes a chosen task by the user
def task_deleter(List_of_Tasks):
    userInput = input("What task do you want to delete? Input the exact name.")
    if userInput in List_of_Tasks:
        print(f"'{userInput}' has been deleted.")
        del List_of_Tasks[userInput]
    else:
        print("Task not recorded.")

#marks the chosen task as Done
def task_marker(List_of_Tasks):
    while True:
        try:
            userInput = input("What task do you want to mark done?: ")
            if userInput in List_of_Tasks:
                if List_of_Tasks[userInput] == "Done.":
                    undoneTask = ("Task is already done. Mark undone? Yes or No:")
                    if undoneTask.strip().lowercase() == "yes":
                        List_of_Tasks[userInput] == "Done"
                        print(f"'{userInput}' marked as undone.")
                        return
                    elif undoneTask.strip().lowercase() == "no":
                        print("noted.")
                        return
                else: 
                    List_of_Tasks[userInput] == "Done."
                    print(f"'{userInput}' marked as done.")
                    return
            else:
                print("There's no such task.")
        except ValueError:
            print("Invalid Input.")

#checks if the tasks are done or not done
def status_checker(List_of_Tasks):
    task_done = 0
    task_not_done = 0
    for value in List_of_Tasks.items():
        if value.lowercase() == "Done":
            task_done += 1
        elif value.lower.case() == "Not Done":
            task_not_done += 1
        else:
            continue
    if task_done == len(List_of_Tasks):
        userStatus = 1
    else: 
        userStatus = 2
    return userStatus,task_done,task_not_done

#ends the program and prints ending messages
def program_ender(List_of_Tasks):
    userStats,finished_task,unfinished_task = status_checker(List_of_Tasks)
    print(f"You have {finished_task} tasks done and {unfinished_task} tasks not done.")
    if userStats == 1:
        print("Good Job! You finished all your tasks!")
    elif userStats == 2:
        print("Go finish your tasks!")

#the main controller, loops with itself and uses the other functions
def main_menu(task_adder, task_viewer, task_marker, task_deleter, program_ender):
    userChoice = "0"
    while userChoice != "5" or 5: 
        userChoice = "0"
        print("What do you want to do?")
        menu_choices = {"Add task" : 1, "View Current Tasks" : 2, "Delete Task" : 3, "Mark a task Done": 4, "End the Program": 5 }
        for index,(key, value) in enumerate(menu_choices.items(),1):
            print(f"{index}. {key}. {value}")
        userChoice = input ("Press the corresponding number. ")
        if userChoice == "1":
            task_adder(List_of_Tasks)
            main_menu(task_adder, task_viewer, task_marker, task_deleter,program_ender)
        elif userChoice == "2":
            task_viewer(List_of_Tasks)
            main_menu(task_adder, task_viewer, task_marker, task_deleter,program_ender)
        elif userChoice == "3":
            task_deleter(List_of_Tasks)
            main_menu(task_adder, task_viewer, task_deleter, task_marker, program_ender)
        elif userChoice == "4":
            task_marker(List_of_Tasks)
            main_menu(task_adder, task_viewer, task_deleter, task_marker, program_ender)
        else: 
            print("Invalid Input.")
            main_menu(task_adder, task_viewer, task_deleter, task_marker, program_ender)
    else:
        print(" ")


#main function
task_getter(List_of_Tasks)#gets the tasks
main_menu(task_adder, task_viewer, task_deleter, task_marker, program_ender)
program_ender(List_of_Tasks)



