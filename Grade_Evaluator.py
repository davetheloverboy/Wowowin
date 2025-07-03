#Grade Evaluator: gives average of the grades of the user then determines if it passes or fails
#ill use for loop instead of while loop

#initializing the dictionary
ListOfGrades = { }

#welcome message
grades_num = 0
gradesSum = 0
final_average = 0
grades_num = input("Hi! How many grades do you want me to evaluate?: ")

for i in range(int(grades_num)): 
    subject_name = input("Input the name of the subject: ")
    subjectGrade = input("Input the grade of that subject: ")

    ListOfGrades[subject_name] = subjectGrade

print("\nThese are your Grades\n")
for key, value in ListOfGrades.items():
    print(f"{key} : {value}")
 
for key,value in ListOfGrades.items():
    grade = int(value)
    gradesSum += grade

final_average = gradesSum / int(grades_num)
print(f"Your average is {final_average}")

passing_grade = 75
if final_average > passing_grade:
    print("You passed!")
else:
    print("You failed")




