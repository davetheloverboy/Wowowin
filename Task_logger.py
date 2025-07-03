# Task logger, make the user input data and then the program prints it out.
# the inputs are put into a list and then printed out. 
# I'll use a loop to print the values of each key in the list

#list initiator
ListOfTasks = [ ] 

print("Input the task that you will do today: ")

#task receiver 
while True:
    task = input("Input 'yes' to end. ")
    if task.strip().lower() == "yes":
        break
    else:
        try:
            InputtedTask = task
            ListOfTasks.append(InputtedTask) 
        except ValueError:
            print("Invalid Input")

#printing the values in the list
print(" \n")
for value in ListOfTasks:
    print(f"{value}.\n")




