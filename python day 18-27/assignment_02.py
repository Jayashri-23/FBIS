# Assignment 02

# Q.1 Store your name in a string variable and print it using f-string.
name = "Jayashri"
print(f"Name:" ,name)

# Q.2 Print your city name using string concatenation.
city = "Nashik"
print("My city is:" + city)

# Q3. Print: "Hello" and "World" on two separate lines using escape character.
print("Hello \n World!")

# Q4. Print a sentence that contains a single quote using escape character.
print('It\'s a beautiful place.')

# Q.5 Print a tab space between two words using escape character.
print("Hello\tWorld")

# Q.6 Check and print the boolean value of 100.
num1 = 100
print(bool(num1))

# Q 7.Check and print the boolean value of 0.
num2 = 0
print(bool(num2))

# Q8.Compare two numbers and print whether first is greater than second.
j = 15
k = 10
print("j is greater than k : ", j > k)

# Q 9.Add two numbers and print the result.
num3 = 10
num4 = 5
sum = num3 + num4
print("Sum is :", sum)

# Q 10. Multiply two numbers and print the result.
x = 3
y = 2
multiplication = x * y
print("Multiplication is :" , multiplication)

# Q 11.Find remainder of 25 divided by 4.
print("Remainder of 25 divided by 4 is :", 25 % 4)

# Q 12.Use += operator to increase a variable by 10.
num5 = 20
num5 += 10
print("increased variable by 10 is:" , num5)

# Q 13.Use -= operator to decrease a variable by 5.
num6 = 20
num6 -= 5
print("decreased variable by 5 is:" , num6)

# Q 14.Compare two numbers using == operator and print result.
num7 = 20
num8 = 20
print(num7 == num8)

# Q 15. Use logical and to check if a number is greater than 10 and less than 20.
num = 15
print(num > 10 and num < 20)

# Q 16. Take two numbers from user and print sum, difference, product, and division.
num9 = int(input("Enter first number:"))
num10 = int(input("Enter second number:"))
print("Sum is :", num9 + num10)
print("Difference is:" , num9 - num10)
print("Product is :" , num9 * num10)
print("Division is :" , num9 / num10)

# Q 17. Print a formatted string that includes name and age using f-string.
name = "Jayashri"
age = 20
print(f"My name is {name} and I am {age} years old.")

# Q 18. Check whether a number entered by user is greater than 50 and print True/False.
num11 = int(input("Enter a number:"))
print(num11 > 50)

# Q 19. Use logical or to check if a number is less than 10 or greater than 100.
num12 = 5
print(num12 < 10 or num12 > 100)

# Q 20 . Use logical not to reverse a comparison result.
num13 = 10
print (not(num13 > 5))

# Q 21.Use identity operator is to compare two variables referencing same list
list1 = ["jayashri", "jay" , "khushi" , "ayush"]
list2 = list1
print(list1 is list2)

# Q 22.Use identity operator is not to compare two different lists.
list3 = ["apple" , "banana" , "grapes"]
list4 = ["apple" , "banana" , "grapes"]
print(list3 is not list4)

# Q 23.Perform bitwise AND on two numbers 5 and 3.
p = 5
q = 3
print("Bitwise AND is:", p & q)

# Q 24. Perform bitwise OR on two numbers 7 and 4
m = 7
n = 4
print("Bitwise OR is:" , m | n)

# Q 25.Perform bitwise XOR on two numbers 6 and 2.
r = 6
s = 2
print("Bitwise XOR is:" , r ^ s)

# Q 26. Take three numbers and evaluate: a + b * c - a // b ** 2   and print the result following operator precedence.
a = 5
b = 3
c = 2
result = a + b * c - a // b ** 2
print("Output is :" , result)

# Q 27. Take a number from user and check:
# * It is greater than 10
# * It is even
#   Print result using logical and.
num14 = int(input("Enter a number:"))
result1 = num14 > 10
result2 = num14 % 2 == 0
print("Number is greater than 10:", result1)
print("Number is even:", result2)
print("Number is greater than 10 and even:", result1 and result2)

# Q 28. Create two lists, assign one list to another variable, then check identity using is and print result.
names1 = ["mango" , "orange" , "banana"]
names2 = names1
print("Check identity using is:" , names1 is names2)

# Q 29.Take two integers, convert them to binary using bitwise operations, then perform AND, OR, and XOR and print results.
int1 = 5
int2 = 10
print("Bitwise AND :", int1 & int2)
print("Bitwise OR :" , int1  | int2)
print("Bitwise XOR :" , int1 ^ int2)

# Q 30. Write a program that:
# * Takes two numbers
# * Uses arithmetic, comparison, logical, and assignment operators in one program
# * Prints at least 6 different outputs.
num15 = int(input("Enter first number:"))
num16 = int(input("Enter second number:"))
print("Addition is:" , num15 + num16)
print("Multiplication is :" , num15 * num16)
print("Is first number greater than second :" , num15 > num16)
print("Is first number less than 50 :" , num15 < 50)
print("Logical AND :" , num15 > 10 and num16 > 10)
print("Logical OR :" , num15 > 10 or num16 > 10)
num16 += 5
print("After increasing num16 by 5, value is :" , num16)
num15 *= 2
print("After multiplying num15 by 2 : " , num15)

