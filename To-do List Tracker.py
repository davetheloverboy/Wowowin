#this program ask for data in a dictionary
#it can add,view, check the tasks if done, delete tasks, and exit the program manually
#for the basic Ill do the input taker, adder, and viewer.

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



#version 2

