#Grade Evaluator: gives average of the grades of the user then determines if it passes or fails
#ill use for loop instead of while loop

#initializing the dictionary



#V1

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







