#Grade Evaluator: gives average of the grades of the user then determines if it passes or fails
#ill use for loop instead of while loop


"""
#V1

#initializing the dictionary
ListOfGrades = { }

#welcome message and initialization
grades_num = 0
gradesSum = 0
final_average = 0
grades_num = input("Hi! How many grades do you want me to evaluate?: ")

#getting the key value pairs of the subjects - grades
for i in range(int(grades_num)): 
    subject_name = input("Input the name of the subject: ")
    subjectGrade = input("Input the grade of that subject: ")

    ListOfGrades[subject_name] = subjectGrade

#printing the dictionary
print("\nThese are your Grades\n")
for key, value in ListOfGrades.items():
    print(f"{key} : {value}")
 
#getting the sum of the grades
for key,value in ListOfGrades.items():
    grade = int(value)
    gradesSum += grade

#getting the average
final_average = gradesSum / int(grades_num)
print(f"Your average is {final_average}")

#determining if the user passed or failed
passing_grade = 75
print("The passing grade is 75 or higher.")
if final_average >= passing_grade:
    print("You passed!")
    print("Congratulations!")
else:
    print("You failed")
    print("Try harder next time")




"""

#V2 - with proper error handling, better format, clean code, proper use of functions

#Grade Evaluator: gives average of the grades of the user then determines if it passes or fails
#ill use for loop instead of while loop

#intializing the dictionary
Subject_and_Grades = { }

#welcome prints
print("Hi and Welcome!")
print("This program asks for your subjects and their grades")
print("and returns the average with the result of it passing or failing")

#getting the number of subject
def get_Subject_count ( ):
    subjectCount = input("So how many subjects do you wish for me to evaluate?: ")
    return subjectCount

#getting the keys first, by for looping with the number of subs then assigning 0 to each
def getDictKeys (NumOfSubs, Subject_and_Grades):
    for i in range(NumOfSubs):
        subjectName = input("Input the Subject name: ")
        Subject_and_Grades[subjectName] = 0
    
#getting the values of each key with user input
def getDictValues (Subject_and_Grades): 
    for key in Subject_and_Grades: 
        subjectGrade = input(f"Input the grade for the subject {key}: ")
        Subject_and_Grades[key] = subjectGrade
 
#getting TOTAL by adding all the values of the dictionary and totalling them
def get_total(Subject_and_Grades):
    total = 0
    for key,value in Subject_and_Grades.items():
       grade = int(value)
       total += grade
    print(f"Your total is {total}.")
    print(type(total),total)
    return total

#getting the average 
def get_average(totalGrade,NumOfSubs):
    print(type(totalGrade),totalGrade)
    average = totalGrade / NumOfSubs
    print(f"Your grade average is {average}")
    return average

def determine_status(average_grade):
    if average_grade >= 75:
        print("You passed!") 
        print("You did it! Congratulations")
    else: 
        print("Aw, you didn't pass, do better next time")


#main function
NumOfSubs = int(get_Subject_count( ))
getDictKeys(NumOfSubs, Subject_and_Grades)
getDictValues(Subject_and_Grades)
totalGrade = get_total(Subject_and_Grades)
average_grade = get_average( totalGrade,NumOfSubs)
determine_status( )
 





