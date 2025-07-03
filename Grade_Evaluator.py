#Grade Evaluator: gives average of the grades of the user then determines if it passes or fails
#ill use for loop instead of while loop

#initializing the dictionary
ListOfGrades = { }

#welcome message
grades_num = 0
grades_num = input("Hi! How many grades do you want me to evaluate?")

for i in range(int(grades_num)): 
    subject_name = input("input the name of the subject")
    subjectGrade = input("input the grade of that subject")

    ListOfGrades[subject_name] = subjectGrade

print(ListOfGrades)

