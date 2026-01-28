# Assignment - 03

#  1. Write a Python program to create a list of 5 student names and print it
studentnames = ["Jayashri" , "khushi" , "bhakti" , "Anushka" , "Ragini"]
print("List of student names:", studentnames)

# 2. Write a program to find the length of a list using len().
print("Length of list is:" , len(studentnames))

# 3. Create a list with mixed data types and print all elements one by one.
list = ["Jayashri" , 45 , 5.6 , True , "Khushi"]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

# 4. Write a program to access the first and last element of a list.
print("First element is :", studentnames[0])
print("Last element is :" , studentnames[-1])

# 5. Create a list and print the element using negative indexing
print(studentnames[-1])
print(studentnames[-2])
print(studentnames[-3])
print(studentnames[-4])
print(studentnames[-5])

# 6. Write a program to check whether "Chetan" exists in a list
print("Chetan" in studentnames)

# 7. Write a program to change the second element of a list.
studentnames[1] = "Rajashree"
print("New list :" , studentnames)

# 8. Create an empty list and append three values to it
emptylst = []
emptylst.append("Rohit")
emptylst.append(45)
emptylst.append(True)
print("New List :" , emptylst)

# 9. Write a program to remove the last element from a list
emptylst.pop()
print("List after removing last element:", emptylst)

# 10.Create a list and clear all its elements using a method.
stdlist = ["Amit" , "Sumit" , "Rohit"]
stdlist.clear()
print("Cleared List is :",stdlist)

# 11. Write a program to slice a list from index 2 to 5.
rollno = [1,2,3,4,5,6,7,8,9,10]
print("Sliced List is :" , rollno[2:6])

# 12. Write a program to replace the first two elements of a list using range assignment.
stdnames = ["Jayashri" , "khushi" , "bhakti" , "Anushka" , "Ragini"]
stdnames[0:2] = ["Aarti" , "Pooja"]
print("Updated list is :", stdnames)

# 13. Create two lists and join them using the + operator.
list1 = ["Jayashri" , "komal" , "Diksha" , "Rajashri"]
list2 = [ 10 , 20 , 30 , 40]
joinedlist = list1 + list2
print(joinedlist)

# 14. Write a program to insert an element at index 3 in a list
list1.insert(3 , "Jayashri")
print("list after inserting element at index 3 :" ,list1)

# 15. 15. Write a program to extend a list using:
# * another list
# * a tuple
list1 = ["Jayashri" , "komal" , "Diksha" , "Rajashri"]
list2 = [1,2,3,4]
list1.extend(list2)
print("Extended list from list2 is :" , list1)

tuple1 = ("Rohit" , "Summit")
list1.extend(tuple1)
print("Extended list from tuple is :" , list1)

# 16. Write a program to remove a specific value from a list using remove().
list3 = ["Jayashri" , "komal" , "Diksha" , "Rajashri"]
list3.remove("Diksha")
print("After removing Diksha :" , list3)

# 17. Write a program to sort a list of integers in ascending order.
rollnolst = [13 , 10 ,45, 1 ,7 ,36 ,55]
rollnolst.sort()
print("Sorted rollnolst is :" , rollnolst)

# 18. Write a program to sort a list of integers in descending order.
rollnolst.sort(reverse=True)
print("sorted list in descending order :" , rollnolst)

# 19. 19. Write a program to reverse a list using an inbuilt method.
rollnolst.reverse()
print("Reversed List is  :" , rollnolst)

# 20. Write a program to copy a list using the copy() method and show that changes in the original list do not affect the copied list.
oldlist = ["Jayashri" , "Anushka" , "Ragini"]
newlist = oldlist.copy()
print("oldlist is :" , oldlist)
print("newlist using copy is :",newlist)

oldlist.append("Komal")
print("After adding element to oldlist is :" , oldlist)
print("newlist remains the same :" , newlist)

# 21. Write a program to extend a list using a dictionary and print the result.
list4 = ["Jayashri" , "komal" , "Diksha" , "Rajashri"]
dict1 = {1:"Rohit" , 2:"Sumit"}
list4.extend(dict1)
print("Extended list using Dict1 is :" , list4)

#  22. Write a program to demonstrate that list2 = list1 creates a reference, not a copy.
list5 = ["Amit" , "Sumit" , "Rohit"]
list6 = list5
print("list5 is :" , list5)
print("list6 is :" , list6)

list5.append("Jayashri")
print("After adding element to list5 :" , list5)
print("Reflected changes in list6:" , list6)

# 23. Write a program to sort a list containing both uppercase and lowercase letters alphabetically
stdname = ["jayashri" , "Komal" , "diksha" , "Rajashri"]
stdname.sort()
print("Alphabetically sorted list is :" , stdname)

# 24. Write a program to sort a list containing uppercase and lowercase letters together using key=str.lower.
stdname = ["jayashri" , "Komal" , "diksha" , "Rajashri"]
stdname.sort(key=str.lower)
print("Alphabetically sorted list using key=str.lower is :", stdname)

# 25. Write a program to remove the element at index 4 using pop().
list7 = ["Jayashri" , "komal" , "Diksha" , "Rajashri" , "Anushka" , "Ragini"]
list7.pop(4)
print("List after removing element :" , list7)

# 26.Write a program to delete the third element of a list using the del keyword.
list7 = ["Jayashri" , "komal" , "Diksha" , "Rajashri" , "Anushka" , "Ragini"]
del list7[2]
print("list after deleting third element :" , list7)

#  27. Write a program to count how many times a specific value occurs in a list.
list8 = ["Jayashri" , "komal" , "Diksha" , "Rajashri" , "Anushka" , "Ragini" , "Jayashri"]
count = list8.count("Jayashri")
print("Count of Jayashri in list is :" , count)

#  28. 28. Write a program to find the index of a specific element in a list.
list9 = ["Jayashri" , "komal" , "Diksha" , "Rajashri" , "Anushka" , "Ragini"]
print("Index of Diksha is :" , list9.index("Diksha"))

# 29. Write a program to add elements of a set to a list using extend().
list10 = ["Jayashri" , "komal" , "Diksha"]
set1 = {"Rohit" , "Sumit" , "Rahul"}
list10.extend(set1)
print("List after extending set :" , list10)

# 30.30. Write a program that performs the following operations on a list:
# * append
# * insert
# * remove
# * sort
# * reverse
list11 = ["komal" , "Diksha", "Rajashri" , "Sanika" ,"Supriya" , "Yogini" , "Rutuja"]
list11.append("Jayashri")
print("After appending Jayashri :" , list11)
list11.insert(2 , "Rinal")
print("After inserting Rinal at index 2 :" , list11)
list11.remove("Sanika")
print("After Removing sanika :" , list11)
list11.sort()
print("After Sorting the list :" , list11)
list11.reverse()
print("After Reversing the list :" , list11)
