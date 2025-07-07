# Task logger, make the user input data and then the program prints it out.
# the inputs are put into a list and then printed out. 
# I'll use a loop to print the values of each key in the list

#list initiator
ListOfTasks = [ ] 
number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 

print("Input the task that you will do today: ")

#task receiver 
while True:
    task = input("Input 'end' to end. ")
    if task.strip().lower() == "end":
        break
    else:
        try:
            InputtedTask = task
            ListOfTasks.append(InputtedTask) 
        except ValueError:
            print("Invalid Input")

#printing the values in the list
print("These are your listed tasks for today.")
print(" \n")
for i,task in enumerate(ListOfTasks):
    print(f"{i+1}. {task}.\n")




