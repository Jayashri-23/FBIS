# # 1. Write a program to print all odd numbers from 1 to 50, but skip numbers divisible by 5 using continue.

# for i in range(1,51):
#     if i % 2 != 0:
          
#         if i % 5 == 0:
#             continue
#         print(i)

# # 2.Write a for loop that prints numbers from 1 to 100, but stops completely when a number divisible by both 7 and 9 is found
 
# for i in range(1,100):
#     if i % 7 == 0 and i % 9 == 0:
#             break
#     print(i, end=" ")
            
# #3.Using a while loop, print numbers from 10 to 1, but skip number 6
# num = 10
# while num >= 1:
#      if num == 6:
#            num-= 1
#            continue
#      print(num)
#      num -= 1

# # 4.Write a program to iterate through a list of names and stop printing once the name "admin" is found.     
# namelist = ["ram","sham","gita","admin","sita","shiv"]
# for i in namelist:
#     if i == "admin":
#         break
#     print(i)

# # 5. Write a program to print the first 5 even numbers using a while loop 
# num = 2
# while num <= 10:
#     print(num)
#     num += 2
           
# #6. Write a loop that prints characters of a string, but does not print vowels
# string1 = "hello world"
# for i in string1:
#     if i in "aeiou":
#         continue
#     print(i)    

# # 7. Write a program using for loop and else to check whether a number exists in a list.
# lst = [1,2,3,4,5]
# num = 4
# for i in lst:
#     if i == num :
#         print("4 is exist in list.") 
#     break 
# else:
#     print("4 is not exist in list.")

# # 8. Write a program that prints numbers from 1 to 20, but prints "Skipped" instead of the number 13.
# for i in range(1,21):
#     if i == 13:
#         print("Skipped")
#         continue
#     print(i)         

# # 9. Write a loop that prints numbers from 1 to 10, but uses pass for even numbers
# for i in range(1,11):
#     if i % 2 == 0:
#         pass
#     else:
#         print(i)

# # 10.Write a program that counts how many numbers between 1 and 100 are divisible by 3
# count = 0
# for i in range(1,101):
#     if i % 3 == 0 :
#         count += 1
# print(f"There are {count} numbers between 1 to 100 divisible by 3.") 

# # 11.Write a program to find the first number between 1 and 1000 that is divisible by 11 and 13, then stop the loop.
# for i in range(1,1000):
#     if i % 11 == 0 and i % 13 == 0 :
#         break
# print(f"The first number between 1 and 1000 that is divisible by 11 and 13 is {i}")

# # 12. Write a program that prints all numbers from 1 to 100, but:
# # Skip multiples of 3
# # Stop if a number divisible by 17 appears  

# for i in range(1,100):
#     if i % 3 == 0:
#         continue
#     if i % 17 == 0:
#         break
#     print(i)

# # 13. Using a while loop, keep taking numbers from the user until they enter 0, then print how many numbers were entered    

# count = 0
# while True:
#     num = int(input("Enter a number : "))
#     if num == 0:
#         break
#     count += 1
# print("Total numbers entered : ",count)  

# # 14.Write a program to check whether a given number is prime, using a loop and break.
num = int(input("Enter number: "))

if num <= 1:
    print("Not Prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime number")
            break
    else:
        print("Prime number")


# # 15 . Write a program that prints a triangle pattern using nested for loops.
# row = 5
# for i in range(1 , 6):
#     for j in range(i):
#         print("*" , end=" ")
#     print()   


# # 16. Write a program to iterate through a list of integers and print **only the first negative number, then stop.
# lst = [1,2,3,4,-5,6,7]
# for i in lst:
#     if i < 0:
#         print("**")
#         break
#     else:
#         print(i)

# # 17. Write a program using for-else to check if a number is present in a range from 1 to 50.
# num = int(input("Enter number: "))
# for m in range(1,50):
#     if m ==  num:
#         print("Number is present.") 
#         break
# else:
#     print("Nmuber is not present.")

# # 18. Write a program that skips all numbers divisible by 4, but prints all others from 1 to 40.
# for i in range(1,40):
#     if i % 4 == 0:
#          continue
#     print(i)

# # 19. Write a program that finds the “sum of numbers until the sum becomes greater than 100”, then stops.
# sum = 0
# while sum <= 100 :
#     num = int(input("Enter a number : "))
#     sum += num
# print("Sum is greater than 100.")
# print(sum)    

# # 20. Write a program that prints numbers from 1 to 100, but replaces:

# #  multiples of 3 → "Fizz"
# #  multiples of 5 → "Buzz"
# #  multiples of both → "FizzBuzz"
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz") 
#     elif  i % 3 == 0 :
#         print("Fizz")
#     elif i % 5 == 0 :
#         print("Buzz")
#     else:
#         print(i)

# # 21. Login Attempts System
#     # A user gets 3 attempts to enter the correct password.
#     # Stop the loop if the password is correct, otherwise block access

# correct_pass = "admin@123"
# for i in range(1,4):
#     password = input("Enter password : ")
#     if password == correct_pass :
#         print("Login Successful ✅")
#         break
#     else:
#         print("Wrong Password ❌")
# else:
#     print("Block Access 🚫")

# # 22. ATM Withdrawal
#     # Keep asking for withdrawal amount until the amount is less than or equal to balance.
# bal = 5000
# while True:
#     amt = int(input("Enter amount: "))
#     if amt <= bal :
#         print("Amount Withdrawl successful.")
#         break


# # 23. Student Attendance
#     # Iterate through a student list and stop checking attendance when "absent" is found.

# attendance = ["present","present","present","absent","present"]
# for i in attendance:
#     if i == "absent":
#         break
#     print(i)
    
# # 24. Online Exam System
#     # Skip a question if the student chooses "skip" and continue to the next question.
# question = ["Q.1","Q.2","Q.3","Skip","Q.5"]
# for n in question:
#     if n == "Skip":
#         continue    
#     print(n)

# # 25. Inventory Check
#     # Loop through product quantities and stop when *stock reaches zero*    
# product_quantity = [10,5,6,9,8,0,6,7]
# for i in product_quantity:
#     if i == 0:
#         break
#     print(i)

# # 26. OTP Verification
#     # Users have 5 chances to enter OTP. Stop immediately when OTP matches

# otp = "1234"
# for i in range(1,6):
#     user = input("Enter OTP : ")
#     if user == otp:
#         print("OTP Verified")
#         break

# # 27.  Website Visitor Counter
#     # Count visitors until count reaches 100, then stop the loop
# count = 0
# while count < 100:
#     count += 1
#     print(f"Visitor {count}")
# print("Limit Reached.")  


# # 28. Salary Processing
#     # Skip employees whose salary is 0, process others 

# salary = [30000,33000,43000,10000,0,25000]
# for i in salary:
#     if i == 0:
#         continue
#     print("Processed : ",i)

# # 29. Menu-Driven Program 
# # Show menu repeatedly until user selects "Exit".

# while True:
#     User = input("Enter your choice(Exit-to stop) :")
#     if User == "Exit":
#         break

# # 30. Game Lives System 
# # The player has 3 lives. Each wrong move reduces one life. End game when lives become 0.
# lives = 3
# while lives > 0 :
#     move = input("Enter Your move (Wrong/Right) : ")
#     if move ==  "Wrong":
#         lives -= 1 
#     if lives == 0:
#       print("Gamr Over...")    

