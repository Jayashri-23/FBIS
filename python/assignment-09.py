
# Assignment - 09 

# Q.1 Write a program to check whether a number is positive or negative.
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# Q.2 Write a program to check if a number is greater than 100.
num = int(input("Enter a number: "))
if num > 100:
    print("The number is greater than 100. ")
else:
    print("The number is not greater than 100. ") 

# Q.3 Write a program to check whether a given number is even or odd
number1 = int(input("Enter a number: "))
if number1 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Q.4 Write a one-line if statement to check if a number is less than 50
num1 = int(input("Enter a number: "))
if num1 < 50:
    print("The number is less than 50.")

# Q.5 Write a program to check whether a person is eligible to vote (age ≥ 18)
age = int(input("Enter your age : "))
if age >= 18 :
    print("You are eligible to vote. ")
else:
    print("You are not eligible to vote. ")

# Q.6 Write a program to check whether a number is positive, negative, or zero.
num2 = int(input("Enter a number: "))
if num > 0:
    print("The number is positive. ")
elif num2 < 0:
    print("The number is negative. ")
else :
    print("The number is zero. ")

# Q.7 Write a program to check the largest of two numbers
num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))
if num3 > num4:
    print("The Largest number is: ", num3)
else:
    print("The largest number is : ", num4)   

# Q.8 Write a program to check the largest of three numbers using if-elif
num5 = int(input("Enter first number: "))
num6 = int(input("Enter second number: "))
num7 = int(input("Enter third number: "))

if num5 >= num6 and num5 >= num7:
    print("The Largest number is: ", num5)
elif num6 >= num5 and num6 >= num7:
    print("The Largest number is: ", num6)
else:
    print("The Largest number is : ", num7)

# Q.9 Write a program to check whether a year is a leap year    
year = int(input("Enter a year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")    
else : 
    print(f"{year} is not a leap year.")

#  Q.10  Write a program to check if a student passed or failed (marks ≥ 40)
marks = int(input("Enter your Marks: "))
if marks >= 40:
    print("You have Passed the exam. ")
else:
    print("You have Failed the exam. ")

# Q.11. Write a program to assign grades:
    #    ≥90 → A
    #    ≥75 → B
    #    ≥60 → C
    #    Else → Fail    
marks1 = int(input("Enter your Marks : "))
if marks1 >= 90:
    print("Grade A")
elif marks1 >= 75:
    print("Grade B")
elif marks1 >= 60:
    print("Grade C")
else:
    print("Fail")

# Q.12 Write a program to check whether a number lies between 10 and 50 using and.
num8 = int(input("Enter a number: "))
if num8 >= 10 and num8 <= 50:
    print("The number lies between 10 and 50.")
else:
    print("The number does not lie between 10 and 50.")

#  Q.13  Write a program to check whether at least one condition is true using or.
num9 = int(input("Enter a number: "))
if num9 < 0 or num9 > 100:
    print("The number is either less than 0 or greater than 100.")
else:
    print("The number is between 0 and 100.")

# Q. 14 Write a program to check login:
#         username = "admin"
#         password = "1234"
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Login Failed.")

# 15. Write a program to check if a number is divisible by 3 and 5
num10 = int(input("Enter a number : "))
if num10 % 3 == 0 and num10 % 5 == 0:
    print("The number is divisible by 3 and 5.")
else:
    print("The number is not divisible by 3 and 5.")

# Q. 16 Write a nested if program to check:
        # gender = female
        # age ≥ 18 → Can vote
gender = input("Enter gender : ")
age1 = int(input("Enter your age : "))
if gender == "female":
    if age1 >= 18 :
        print("You can vote.")
    else:
        print("You cannot vote.")
else:
    print("You cannot vote.")

# Q.17 Write a program to check whether a character is a vowel or consonant.
character = input("Enter a character : ")
if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
    print("Vowel")
else:
    print("Consonant")

#  Q.18 Write a one-line if-else to check pass/fail.

marks1 = int(input("Enter your marks: ")) 
print("Pass") if marks1 >= 40  else print("Failed")

# Q.19 Write a program using not operator to reverse a condition
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
if not a > b :
    print("a is not less than b")

# Q.20 Write a program that uses pass inside an if block and print “Thank you” in else.
num5 = int(input("Enter age :"))
if num5 < 0 :
    pass
else :
    print("Thank you")

# Q.21 Write a program using match to print the day name for numbers 1–7.
day = int(input("Enter day number from 1-7 : "))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3 :
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _ :
        print("Invalid day number , Good day!")

# Q.22 Write a program using match to build a simple calculator (+, -, *, /)
p = int(input("Enter first number : "))
q = int(input("Enter second number : "))
operators = input("Enter operator(+, - , *, /) : ")
match operators:
    case "+":
        print(p+q)
    case"-":
        print(p-q)
    case"*" :
        print(p*q)
    case"/":
        print(p/q)
    case _:
        print("Invalid operator")

# Q.23 Write a program to categorize age:
        # <13 → Child
        # 13–19 → Teen
        # 20–59 → Adult
        # 60+ → Senior            
age = int(input("Enter age : "))
if age < 13 :
    print("Child")
elif age >= 13 and age <= 19 :
    print("Teen")
elif age >= 20 and age <= 59 :
    print("Adult")
else:
    print("Senior")

# Q.24 Write a program using match to check month name from month number   
month =  int(input("Enter a month number : "))
match month:
    case 1 :
        print("January") 
    case 2 :
        print("February")
    case 3 :
        print("March")
    case 4 :
        print("April")
    case 5 :
        print("May")
    case 6 :
        print("June")
    case 7 :
        print("July")
    case 8 :
        print("August")
    case 9 :
        print("September")
    case 10 :
        print("October")
    case 11 :
        print("November")
    case 12 :
        print("December")
    case _ :
        print("Invalid month number")

# Q.25 Write a program using a match with a default case and print “Month number is not present”   
month  = int(input("Enter month number : "))
match month:
    case 1 :
        print("January")
    case 2 :
        print("February")   
    case 3 :
        print("March")
    case 4 :
        print("April")
    case _ :
        print("Month number is not present.")   

# Q.26 Write a program to check traffic signal colors and print actions
color = input("Enter traffic signal color(eg. Red , Yellow , Green) : ")
if color == "Red" :
    print("Stop")
elif color == "Yellow" :
    print("Get Ready")
elif color == "Green" :
    print("Go")
else :
    print("Invalid color")

#Q.27 Write a program using match to classify student group based on name list.
name  = input("Enter student name : ")
match name :
    case "ayush" |" omkar" | "jayashri" :
        print("Group A")
    case "ragini" | "anushka" | "kushi" :
        print("Group B")
    case "rohit" | "komal" | "rim" :
        print("Group C")
    case _ :
        print("Student not in list.")

#28. Write a program to check eligibility for a job:
        # Age ≥ 21
        # Degree = Yes
        # Experience ≥ 1 year 

age = int(input("Enter your age : "))
degree = input("Do you have degree (Yes/No) : ")
experience = int(input("Enter your experience in years : "))

if age >= 21 and degree == "Yes" and experience >= 1 :
    print("Eligiblle for job.")
else :
    print("Not eligible for job.")

# Q.29 Write a program using match with multiple values in one case    
number = int(input("Enter the number : "))
match number :
    case 1 | 2 | 3 | 4 :
        print("The number between 1 to 4 range.")
    case 5 | 6 | 7 | 8 :
        print("The number between 5 to 8 range.")
    case _ :
        print("The number is out of range.")        
   