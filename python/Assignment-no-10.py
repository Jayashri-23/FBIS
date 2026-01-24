# 1. Write a program to print all odd numbers from 1 to 50, but skip numbers divisible by 5 using continue.

# for i in range(1,51):
#     if i % 2 != 0:
          
#         if i % 5 == 0:
#             continue
#         print(i)

# 2.Write a for loop that prints numbers from 1 to 100, but stops completely when a number divisible by both 7 and 9 is found
 
# for i in range(1,100):
#     if i % 7 == 0 and i % 9 == 0:
#             break
#     print(i, end=" ")
            
#3.Using a while loop, print numbers from 10 to 1, but skip number 6
# num = 10
# while num >= 1:
#      if num == 6:
#            num-= 1
#            continue
#      print(num)
#      num -= 1

# 4.Write a program to iterate through a list of names and stop printing once the name "admin" is found.     
# namelist = ["ram","sham","gita","admin","sita","shiv"]
# for i in namelist:
#     if i == "admin":
#         break
#     print(i)

# 5. Write a program to print the first 5 even numbers using a while loop 
# num = 2
# while num <= 10:
#     print(num)
#     num += 2
           
#6. Write a loop that prints characters of a string, but does not print vowels
# string1 = "hello world"
# for i in string1:
#     if i in "aeiou":
#         continue
#     print(i)    

# 7. Write a program using for loop and else to check whether a number exists in a list.
# lst = [1,2,3,4,5]
# num = 4
# for i in lst:
#     if i == num :
#         print("4 is exist in list.") 
#     break 
# else:
#     print("4 is not exist in list.")

# 8. Write a program that prints numbers from 1 to 20, but prints "Skipped" instead of the number 13.
# for i in range(1,21):
#     if i == 13:
#         print("Skipped")
#         continue
#     print(i)         

# 9. Write a loop that prints numbers from 1 to 10, but uses pass for even numbers
# for i in range(1,11):
#     if i % 2 == 0:
#         pass
#     else:
#         print(i)

# 10.Write a program that counts how many numbers between 1 and 100 are divisible by 3
# count = 0
# for i in range(1,101):
#     if i % 3 == 0 :
#         count += 1
# print(f"There are {count} numbers between 1 to 100 divisible by 3.") 

# 11.Write a program to find the first number between 1 and 1000 that is divisible by 11 and 13, then stop the loop.
# for i in range(1,1000):
#     if i % 11 == 0 and i % 13 == 0 :
#         break
# print(f"The first number between 1 and 1000 that is divisible by 11 and 13 is {i}")

# 12. Write a program that prints all numbers from 1 to 100, but:
# Skip multiples of 3
# Stop if a number divisible by 17 appears  

# for i in range(1,100):
#     if i % 3 == 0:
#         continue
#     if i % 17 == 0:
#         break
#     print(i)

# 13. Using a while loop, keep taking numbers from the user until they enter 0, then print how many numbers were entered    

# count = 0
# while True:
#     num = int(input("Enter a number : "))
#     if num == 0:
#         break
#     count += 1
# print("Total numbers entered : ",count)  

# 14.Write a program to check whether a given number is prime, using a loop and break.
# num = int(input("Enter number : "))

# for i in num:
#     if i % 2 == 0:
#         print("Not Prime number.")                        # NOT SOLVED
#         break
#     else:
#         print("Prime number.")

# 15 . Write a program that prints a triangle pattern using nested for loops.
row = 5
for i in range(1 , row+1):
    for j in range(i):
        print("*" , end=" ")
    print()   


# 16. Write a program to iterate through a list of integers and print **only the first negative number, then stop.
