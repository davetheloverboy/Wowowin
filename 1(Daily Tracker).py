#Variable + Data Types
#my first version of a daily activity tracker
"""
name = "Dave" 
age = 20
height = "175.25cm"
is_Student = False
hobbies = ["gaming", "watching youtube", "listening to music"]
person = {"name":dave, "age":20}

print(type(name), type(age), type(person), type(hobbies))



#Build a small Python program that tracks basic data about your day, using at least 5 different data types.
Daily_doings= {"name": "Dave", 
               "Productive Hours": 2, 
               "Hours of Sleep": 7.5, 
               "Did you eat on time today?": False, 
               "Your Top 3 Completed Task":[MULTILINE == "Mild Exercise", "Programming Block","Journalling"] 
               } 

print(Daily_doings)
print(Daily_doings["Productive Hours"])
print(Daily_doings["Did you eat on time today?"])
print(Daily_doings["Hours of Sleep"])
print(Daily_doings["name"])
print(Daily_doings["Your Top 3 Completed Task"])



#my second version
#pseudocode = i collect the data through if statements, try catch, store it in a dictionary then print it.

summary = { }
good_condition = ["i'm good","i'm fine","i'm okay","i'm doing great","good","okay","fine"] 
bad_condition = ["not good","not fine","i'm not okay","not okay"]

#for the name
summary["name"] = input("Hi! What's your name?: ")
name = summary["name"]
print(f"What a great name, Hi {name}.")

#for the how are you?
summary["current condition"] = input("How are you now?")
condition = summary["current condition"] 

#for the hours of sleep
summary["hours of sleep"] = int(input("How many hours did you sleep?"))
sleep_duration = summary["hours of sleep"] 
if sleep_duration > 7 and sleep_duration  <= 9:
  print("That's good")
elif sleep_duration > 9:
  print("That's too much!")
elif sleep_duration < 7 and sleep_duration  >= 5:
  print("That's a decent amount of sleep")
else:
  print("Hey sleep properly!")
  
#for the times of eating
summary["eating_frequency"] = input("How many times did you eat today?: ")
summary["OMAD"] = input("Is today an OMAD day?: ")

eat_freq = int(summary["eating_frequency"])
omad = bool(summary["OMAD"])

#productivity
summary["Study_hours"] = input("How many hours did you give to learning?: ")
summary["Exercise_hours"] = input ("How many hours for exercise?: ")
summary["Creativity_hours"] = input ("For your personal creativity?: ")

brain_hours = int(summary["Study_hours"])
body_hours = int(summary["Exercise_hours"])
also_brain_hours = int(summary["Creativity_hours"])

#kaoa-han
summary["movingOnStatus"] = input("Siya parin?: ")
statusMo = bool(summary["movingOnStatus"])

print("So here's your current status: \n")
for key, value in summary.items( ):
  print(f"{key} : {value}")

"""

# okay version 3 na yung ilagay na sa mga functions
# first initialize the dictionary, then make the lists of conditions and other lists
# we'll have 7 functions, name, condition, sleep hours,eating frequency, productivity, kaoahan, and the printing for loop

summary = { }

#for the name
def ask_name( ): 
  name = input("Hi! What's your name?: ")
  print(f"What a great name, Hi {name}.")
  summary["name"] = name

#for the how are you?
def ask_condition( ):
  good_condition = ["i'm good","i'm fine","i'm okay","i'm doing great","good","okay","fine","Im okay","Im fine","Im good"] 
  bad_condition = ["not good","not fine","i'm not okay","not okay","not good","not fine","i don't feel good","i dont feel good","im not okay"]
  condition = input("How are you now?: ")
  if condition.strip().lower() in bad_condition:
    print("aw luoy")
  elif condition.strip().lower() in good_condition:
    print("beri good")
  else: 
    print("?")
  summary["current condition"] = condition

#for the hours of sleep
def ask_sleep( ):
  while True:
    try:
      sleep_duration = int(input("How many hours did you sleep?: ")) 
      if sleep_duration > 7 and sleep_duration  <= 9:
        print("That's good!")
      elif sleep_duration > 9:
        print("That's too much!")
      elif sleep_duration < 7 and sleep_duration  >= 5:
        print("That's a decent amount of sleep")
      else:
        print("Hey sleep properly!")
      summary["hours of sleep"] = sleep_duration
      break
    except ValueError:
      print("Error. Input a number please.")
  
  
#for the times of eating
def ask_eating( ):
  while True:
    try: 
      eat_frequency = int(input("How many times did you eat today?: "))
      summary["eating_frequency"] = eat_frequency
      break
    except ValueError:
      print("Invalid input. Input a number.")
  
  omad = input("Is today an OMAD day?: ")
  while omad.lower().strip() == "yes" or omad.lower().strip() == "no":
    summary["OMAD"] = omad 
    print("Okay noted!")
    break
  else:
    print("Invalid Input. Input yes or no only.")
  

#productivity
def ask_productivity( ):
  while True:
    try:
      brain_hours = int(input("How many hours did you give to learning?: "))
      summary["Study_hours"] = brain_hours
      break
    except ValueError:
      print("Valid Input. Input numbers Only")
  

  while True:   
    try:
      body_hours = int(input("How many hours for exercise?: "))
      summary["Exercise_hours"] = body_hours
      break
    except ValueError:
      print("Valid Input. Input numbers Only")
  

  while True:
    try:
      also_brain_hours = int(input("For your personal creativity?: "))
      summary["Creativity_hours"] = also_brain_hours
      break
    except:
      print("Valid Input. Input numbers Only") 

#kaoa-han
def ask_status( ):
  statusMo = input("Siya parin?: ")
  summary["movingOnStatus"] = statusMo
  print("mao ba")
  
def print_summary(summary):
  print("So here's your current status: \n")
  for key, value in summary.items( ):
    print(f"{key} : {value}")

def solve_productivity_hours(summary):
  productivity_hours = summary['Exercise_hours'] + summary['Study_hours'] + summary['Creativity_hours']
  return productivity_hours

#main function
ask_name( )
ask_condition( )
ask_sleep( )
ask_eating() == summary["eating_frequency"], summary["OMAD"]  #unpacking the tuple
ask_productivity() == summary["Study_hours"], summary["Exercise_hours"], summary["Creativity_hours"]  #unpacking the tuple
productivity_hours = solve_productivity_hours(summary)
ask_status() 

#printing the whole summary
print_summary(summary)
print(f"You had {productivity_hours} productivity hours")







