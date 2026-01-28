#  Assignment No.-06

# Q.1 Create a set with 5 integer values and print it.

numset  = {1, 2, 3, 4,5}
print(numset)

# Q.2 Create a set using the set() constructor from a list.

numset1 = [10 ,20, 30, 40, 50,]
newset =  set(numset1)
print(newset)

# Q.3 Create a set with duplicate values and print the result.

duplicateset = {1,2,3,4,5,5,5,4,6,7,4,4}
print(duplicateset)

# Q.4 Create a set containing True and 1. Print the set.

boolset = {True , 1, 0 ,False}
print("The Boolset is :",boolset)

#  Q.5 Write a program to find the length of a set using len()

numset2 = {10,20,30,40,50,60,70,80,90}
print("Length of set is :", len(numset2))

# Q.6 Create a set with mixed data types and print it.

mixedset = {1, "Jayashri" , 4.5 , True, 6+5j}
print("Mixed set is :", mixedset)

# Q.7 Write a program to access set elements using a for loop

nameset = {"jayashri", "khushabu", "dipti","anushka"}
for i in nameset:
     print(i)

# Q.8 Create an empty set and add three elements using add().

emptyset = set()
emptyset.add("Jayashri")
emptyset.add(45)
emptyset.add(True)
print(emptyset)

# Q.9 Write a program to remove an element from a set using discard()

numset3 = {10,20,30,40,50,60}
numset3.discard(30)
print("Set after removing 30 is :", numset3)

# Q.10 Write a program to remove an element from a set using remove()

numset4 = {100,200,300,400,500}
numset4.remove(200)
print("Set after removing 200 is :", numset4)

# Q.11 Write a program that removes a non-existing element using discard().

numset6 = {1,2,3,4,5,6}
numset6.discard(10)   # No error will be shown
print("Set after discarding non-existing element 10 is :", numset6) 

# Q.12 Write a program that removes a non-existing element using remove() and observe the error

numset7 = {10,20,30,40}
numset7.remove(90)
print("Set after removing non-existing element 90 is :", numset7)  # This will raise a KeyError because 90 is not present in the set.

# Q.13 Write a program to remove a random element from a set using pop().

numset8 = {1,2,3,4,5,6,7,8,9}
numset8.pop()
print("Set after removing a random element is :", numset8)

# Q.14 Write a program to clear all elements from a set using clear().

numset9 = {10,20,30,40,50,60}
numset9.clear()
print("Set after clearing all elements :",numset9)

# Q.15 Write a program to delete a set completely using del.
numset9 = {10,20,30,40,50,60}
del numset9
print(numset9)  # This will raise a NameError because numset9 has been deleted.

# Q.16 Write a program to combine two sets using union()

set1 = {1,2,3,4,5,6}
set2 = {"jayashri", "khushabu", "dipti","diksha","Rajashree"}
combineset = set1.union(set2)
print("New combined set is :" , combineset)

# Q.17 Write a program to combine two sets using the | operator.

set3 = {10,20,30,40}
set4 = {"jayashri", "khushabu", "dipti"}
combineSet = set3 | set4
print("Combined set is :" , combineSet)

# Q.18 Write a program to update one set using another set with update()

set5 = {1,2,3,4}
set6 = {"a", "b", "c"}
set5.update(set6)
print("Updated set is :" , set5)

# Q.19 Write a program to join a set with a list using union().

set7 = {100,200,300}
list1 = [1,2,34,5]
newset1 = set7.union(list1)
print("Joined set and list is :" , newset1)

#  Q.20 Write a program to join three sets using union()

set8 = {1,2,3}
set9 = {"jay", "khushi" , "dipti"}
set10 = {10 , 10.4 , 1 ,45}
combinedset1 = set8.union(set9 , set10)
print("Combined three set is :-" , combinedset1)

# Q.21 Write a program to find common elements between two sets using intersection().

set11 = {1,2,3,4,5}
set12 = {4,5,6,7,8}
commonelement = set11.intersection(set12)
print("Common elements between two set is :-" , commonelement)


# Q.22 Write a program to find common elements between two sets using the & operator.

set13 = {10,20,30,40}
set14 = {10,25,30,45}
set13 & set14
print("Common elements between two set using & operator is :-" , set13 & set14)

# Q.23 Write a program to find intersection between a set and a list using intersection().

set15 = {1,2,3,4,5}
list2 = [4,5,6,7,8]
intersectset = set15.intersection(list2)
print("Intersection set between set and list is :-" , intersectset)

# Q.24 Write a program to update a set using intersection_update().

set16 = {1,2,3,4,5}
set17 = {4,5,6,7,8} 
set16.intersection_update(set17)
print("Set after intersection_update is :-" , set16)

# Q.25 Write a program to find elements present in first set but not in second using difference()

set18 = {10,20,30,40,50}
set19 = {30,40,50,60,70}
diffset = set18.difference(set19)
print("Elements present in first set but not in second is :-" , diffset)

# Q.26 Write a program to find difference between two sets using the - operator.
set20 = {10,20,30,40,50}
set21 = {30,40,50,60,70}
diffset2 = set20 - set21
print("Difference between two sets using - operator is :-" , diffset2)

# Q.27 Write a program to update a set using difference_update()
set22 = {1,2,3,4,5}
set23 = {4,5,6,7,8}
set22.difference_update(set23)
print("Set after difference_update is :-" , set22)

# Q.28 Write a program to find symmetric difference using symmetric_difference()
set24 = {1,2,3,4}
set25 = {3,4,5,6} 
symdiffset = set24.symmetric_difference(set25)
print("Symmetric difference between two sets is :-" , symdiffset)

# Q.29 Write a program to find symmetric difference using the ^ operator.

set26 = {10,20,30}
set27 = {30,40,50}
symdiffset2 = set26 ^ set27
print("Symmetric diff. using ^ operator is :-" , symdiffset2)

# Q.30 Write a program to perform union, intersection, difference, and symmetric difference on two sets and print all results

numset10 = {1,2,3,4,5}
numset11 = {4,5,6,7,8}
unionset = numset10.union(numset11)
intersectset = numset10.intersection(numset11)
diffset3 = numset10.difference(numset11)
symdiffset3 = numset10.symmetric_difference(numset11)
print("Union Of two set is :-", unionset)
print("Intersection of two set is :-", intersectset)
print("Difference of two set is :-", diffset3)
print("Symmetric Difference of two set is :-", symdiffset3)
