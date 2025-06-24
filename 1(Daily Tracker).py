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
"""


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




















