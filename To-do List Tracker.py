#this program ask for data in a dictionary
#it can add,view, check the tasks if done, delete tasks, and exit the program manually
#for the basic Ill do the input taker, adder, and viewer.

#Version 1
#intitialize the dictionary
TaskList = { }

Inputted_task = ""
while Inputted_task != "1":
    print("Press Enter to add the task, Press 1 to see your tasks.")
    Inputted_task = input("Input a task to do. ")
    
    TaskList[Inputted_task] = " not done"

for key,value in TaskList.items():
    print("These are your tasks: ")
    print(f"{key}:{value}")


