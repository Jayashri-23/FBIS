# Q.1 Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i , end = " ",)
    
# Q.2 Print all even numbers between 1 and 20.
for i in range(1,21):
    if i % 2 == 0:
     print("\n",i)

# Q.3 Print all odd numbers from 1 to 15
for i in range(1,16):
      if i % 2 != 0:
         print(i,end=" ")  

# Q.4 Count how many numbers are divisible by 3 between 1 and 50
count = 0
for i in range(1,51):
    if i % 3 == 0:
        print(i,end=" ")
        count += 1
print("\n The Count is :",count)

# Q.5 Find the sum of numbers from 1 to 10.
sum = 0
for i in range(1,11):
    sum += i
print("\n Total sum is :",sum)

# Q.6 Print each character of a string on a new line.
name = "INDIA"
for i in name :
    print(i)

# Q.7 Count how many vowels are present in a given string.
vowel = input("Enter string : ")
count = 0
for i in vowel:
    if vowel in "aeiou":
        print(vowel)
        count += 1
print(count)

# Q.8 Print only uppercase letters from a string.
string = input("Enter string : ")
for i in string:
    if i.isupper():
        print(i)

# Q.9 Reverse a string using a for loop
# name = "INDIA"
# for 



# Q.10 Count digits and letters separately in a string





# Q.11 Find the largest number in a list.
lst = [4, 7, 2, 9]
largest = lst[0]

for i in lst:
    if i > largest:
        largest = i

print(largest)

# Q.12 Find the smallest number in a list
lst1 = [4,7,2,9]
smallest = lst1[0]

for i in lst1:
    if i < smallest:
        smallest = i
print(smallest)

# Q.13 Count how many even and odd numbers are in a list
list1 = [1,2,3,4,5,6,7]
counteven = 0
countodd  = 0
for i in list1:
    if i % 2 == 0:
       
        counteven += 1
      
    else :
        countodd += 1
print("Odd : ",countodd)
print("Even : ",counteven)

# Q.14 





















# While Loop
# Q.1 Write a program to print numbers from 1 to 10 using a while loop.
num2 = 1
while num2 <= 10:
    print(num2)
    num2 += 1

# Q.2 Write a program to print numbers from 10 to 1 using a while loop
n = 10
while n > 0:
    print(n, end=" ")
    n -= 1

#Q.3 Write a program to print all even numbers between 1 and 50 using a while loop
i = 2
while i <= 50:
    print(i)
    i += 2
 
# Q.4 Write a program to print all odd numbers between 1 and 30 using a while loop.
i = 1
while i <= 30:
    print(i,end=" ")
    i += 2 

# Q.5 Write a program to find the sum of numbers from 1 to 100 using a while loop.
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
    print(sum)

# Q.6 Write a program to print the multiplication table of a given number using a while loop. 
  