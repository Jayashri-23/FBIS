# Assignment 07

# Personal Information Collector

name = input("Enter your name:  ")
age = int( input("Enter your age:  "))
gender = input("Enter your gender: ")
city = input("Enter your city: ")
state = input("Enter your state: ")
country = input("Enter your country: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")


print("\n=============================================")
print("\n--- Personal Information Card ---\n")
print("==============================================")
print("Full Name   :",name)
print("Age         :",age)
print("Gender      :",gender)
print("City        :",city)
print("state       :",state)
print("Country     :",country)
print("Email       :",email)
print("Phone Number:",phone)
print("\n=============================================\n")


# Simple Billing System

customer = input("Enter customer name: ")

item1 = input("Item 1 name: ")
item1_price = float(input("Item 1 price: "))

item2 = input("Item 2 name:")
item2_price = float(input("Item 2 price: "))

item3 = input("Item 3 name: ")
item3_price = float(input("Item 3 price: "))

#  calculate Total Amount
total = item1_price + item2_price + item3_price

# Calculate GST (5%)
gst = total * 0.05

# Calculate Final Amount
final_amount = total + gst

print("\n===============================================")
print("\n--- BILL RECEIPT ---\n")
print("\n===============================================")
print("Customer Name :" , customer)
print("Item                            Price(Rs.)")
print("------------------------------------------")
print(f"{item1}                               {item1_price}")
print(f"{item2}                              {item2_price}")
print(f"{item3}                              {item3_price}")
print("-------------------------------------------")
print(f"Total Amount:                     {total}")
print(f"GST(5%):                          {gst}")
print(f"Final Amount:                     {final_amount}")
print("=================================================\n")


# 1. Write a program to add 10 user-entered integers into a list using append(). 
numbers = []
for i in range(10):
           num = int(input("Enter integer : "))
           numbers.append(num)
           print(numbers)


# 2. Append only even integers from 1 to 20 into a list. 
numbers1 = []
for i in range(1, 21):
        if i % 2 == 0:
         numbers1.append(i)
         print(numbers1)

# 3. Display all elements of a list and then clear it.
numlst1 = [1,2,3,4,5,6,7,8,9,10]
print("All Elements of List is :" , numlst1)
numlst1.clear()

# 4. Clear a list and then add 3 new integer values to it.
numlst2 = [11,12,13,14,15]
numlst2.clear()
numlst2.append(100)
numlst2.append(90)
numlst2.append(60)
print("Added 3 New int in list : ",numlst2)

# 5. Clear a list inside a function and print the list outside the function. 





# Copy()

# 1. Copy all elements of one integer list into another list using copy().
numlst3 = [21,22,23,24,25]
numlst4 = numlst3.copy()
print("Original list is : ", numlst3)
print("Copied List is :" , numlst4)

# 2. Copy a list and add new integers to the copied list without affecting the original.
original_lst = [1,2,3,4]
new_lst = original_lst.copy()
print("Copiied list is: ",new_lst)
new_lst.append(20)
new_lst.append(45)
print("Added New elements in new_lst : ", new_lst)
print("Original List is : ", original_lst)

# 3.Copy a list and remove an element from the copied list. 
fruits = ["apple" , "banana" , "mango" , "grapes"]
new_fruit_lst = fruits.copy()
new_fruit_lst.remove("apple")
print("List after removing element :-",new_fruit_lst)

# Count()

# 1. Count how many times the integer 5 appears in a list. 
number = [1,2,3,4,5,6,5,6,5,7,8,5,9]
number.count(5)
print("Count of 5 in list is: ", number.count(5))

# 2.Count the occurrences of a user-entered integer in a list. 




# 3. Count how many times an even number appears in a list.




# extend()

# 1.Extend a list with another integer list entered by the user.
numlist1 = [1,2,3,4,5]
numlist2 = [10,20,30,40]
numlist1.extend(numlist2)
print("Extended list is : " ,numlist1)

# 2.Extend a list using a tuple of integers.



# 3.Extend an empty list with integers from range 1 to 5. 




# index()
# 1. Find the index of a given integer in a list. 
numlst5 = [1,2,3,4,5,6,7,8]
print("index is :",numlst5.index(3) )

# 2.Find the index of the first occurrence of integer 10 in a list. 
numlst6 = [1,10,20,3,0,4,30]
print("index of 10 is :",numlst6.index(10))

# 3. Take an integer from the user and display its index in the list. 




# insert()
# 1.Insert an integer at the beginning of a list.
numlst7 = [2,3,4,5]
numlst7.insert(0,1)
print("List after inserting 1 at beginning :" , numlst7)

# 2.Insert an integer at a specific index entered by the user. 
numlst8 = [1,2,3,4,5]





# 3.Insert the integer 100 at index 3
numlst9 = [10,20,30,40,50]
numlst9.insert(3,100)
print("List after inserting 100 at index 3: " , numlst9)

# Pop()

# 1.Remove the last integer from a list using pop().
numlst10 = [1,2,3,4,5,6,7]
numlst10.pop()
print("popping last element from list:" , numlst10)

# 2.Remove the integer at index 2 using pop().
numlist1 = [1,2,3,4,5]
numlist1.pop(2)
print("popping element of index 2 from list :", numlist1)

# 3.Pop all integers from a list one by one. 
numlist2 = [10,20,30,40,50]
print("length of list is :" , len(numlist2))
numlist2.pop()
numlist2.pop()
numlist2.pop()
numlist2.pop()
numlist2.pop()           # Without loop
print("List after popping all elements :" , numlist2)


# Remove()

# 1. Remove a specific integer value from a list. 
numlist3 = [1,2,3,4,5,6,7]
numlist3.remove(3)
print("New List is :-", numlist3)

# 2. Remove the first occurrence of integer 10 from a list.
numlist4 = [10,20,30,40,50]
numlist4.remove(10)
print("Removing first element from list :" , numlist4)

# 3. Remove all occurrences of a given integer from a list.
numlist5 = [1,2,3,4,5,6,7,8]




# Reverse()
# Reverse an integer list using reverse(). 
numlist6 = [1,2,3,4,5,6]
numlist6.reverse()
print("Reversed list is: " , numlist6)

#  2.  Reverse a list of integers without creating a new list. 
numlist7 = [10,20,30,40,50]
numlist7.reverse()
print("Reversed list is :" , numlist7)

# 3. Reverse a list inside a function





# Sort()
# 1. Sort a list of integers in ascending order.
numlist8  = [12,23,5,1,34,23,45]
numlist8.sort()
print("Sorted List is : " , numlist8)

# 2. Sort a list of integers in descending order.
numlist9 = [34,12,5,67,23,89]
numlist9.sort(reverse = True)
print("Sorted list in desc. order :" ,numlist9)

# Sort a list and display the smallest integer. 
numlist10 = [45,18,33,10,99,46]
numlist10.sort()
print("Smallest integer is : " , numlist10[0])

