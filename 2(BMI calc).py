#let's start with the program making: BMI calculator
#it asks the user for their weight and height and calculates their BMI

weight = float(input("What is your weight?(in kg): "))
height = float(input("What is your height?(in meters): "))
BMI = weight/(height**2) 

category = 0
if BMI < 18.5:
  category = "Underweight"
elif BMI < 25:
  category = "Normal" 
elif BMI < 30:
  category = "Overweight"
else:
  category = "Obese"

print("your BMI is " + str(BMI) +", so your BMI is "+ category +".")
print(f"Your BMI is {str(BMI)} so your BMI is {category}.")

