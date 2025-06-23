#list summarizer, it summarizes the max, min, and average
"""
#the hardcoded part, the list is unchangable
list_of_num= [34,44,51,83,64,45,76,45,86,76,9]

max_value = max(list_of_num)
min_value = min(list_of_num)
average_value = sum(list_of_num)/len(list_of_num)

print(f"The Maximum of this list is {max_value}.")
print(f"The Minimum of this list is {min_value}.")
print(f"The average of this list is {average_value}.")
"""


#harder version, gets an input from the user(the list on numbers) 
#pseudocode : gets input, puts it in a list, uses the list for the list summary 

list_of_num = [ ]
print("Enter numbers for the list")
print("press double enter to end")

while True:
  list_item = input("Input numbers to put inside the list:")
  if list_item == "":
        break
  else:    
    try: 
        value = float(list_item)
        list_of_num.append(value)
    except ValueError:
        print("Invalid input, input numbers only")

Value_max = max(list_of_num)
Value_min = min(list_of_num)
Average = sum(list_of_num)/(len(list_of_num))

print(f"The Maximum number in the list is {Value_max}.")
print(f"The Minimum number in the list is {Value_min}.")
print(f"The Average of the list of numbers is {Average}.")


"""
#this is from gemini, the more perfect version of the code

list_of_num = [ ]
print("Enter numbers for the list")
print("press double enter to end")

while True:
  list_item = input("Input numbers to put inside the list:")
  # Check if the input is an empty string immediately after getting input
  if list_item == "":
        break # Break the loop if the input is empty
  else:
    try:
        value = float(list_item)
        list_of_num.append(value)
    except ValueError:
        print("Invalid input, input numbers only")

# Check if the list is empty before calculating max, min, and average
if list_of_num: # This checks if the list is not empty
    Value_max = max(list_of_num)
    Value_min = min(list_of_num)
    Average = sum(list_of_num)/(len(list_of_num))

    print(f"The Maximum number in the list is {Value_max}.")
    print(f"The Minimum number in the list is {Value_min}.")
    print(f"The Average of the list of numbers is {Average}.")
else:
    print("No numbers were entered to calculate statistics.")

"""


