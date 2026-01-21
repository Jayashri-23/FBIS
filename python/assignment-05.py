#    Assignment No - 05 

# Q.1 Create a tuple with three fruits and print it.
fruits = ("apple", "banana", "cherry")
print(fruits)

# Q.2 Create a tuple with one item Python  and print its type.
tuple_item = ("Python" ,)
print(type(tuple_item))

# Q.3 Create a tuple of five numbers and print its length using len() .
rollnotuple = (1, 2, 3, 4, 5)
print("The lenght of tuple is :", len(rollnotuple))

# Q.4 Create a tuple and print its first element using indexing.
stdnames = ("Jayashri" , "Anushka" , "Bhakti" , "Rinal" , "Khushi")
print(stdnames[0])

# Q.5 Create a tuple and print its last element using negative indexing.
stdnames = ("Jayashri" , "Anushka" , "Bhakti" , "Rinal" , "Khushi")
print("Last Element is :" , stdnames[-1])

# Q.6 Create a tuple using the tuple() constructor with values 1 to 5 and print it.
numtuple = tuple((1,2,3,4,5))
print(numtuple)

# Q.7 Given t = (10, 20, 30, 40, 50) , print elements at index 1 and 3.
t = (10, 20, 30, 40, 50)
print("element at index 1 is :" ,t[1])
print("element at index 1 is :" , t[3])

# Q.8 Given t = ("a","b","c","d","e") , print elements from index 1 to 4 using slicing.
t = ("a","b","c","d","e")
print(t[1:4])

# Q.9 From a tuple t = (5,10,15,20,25,30) , print elements from index 2 to end.
t = (5,10,15,20,25,30)
print(t[2:])

# Q.10 From a tuple t = (5,10,15,20,25,30) , print elements from start to index 3.
t = (5,10,15,20,25,30)
print("elements from start to index 3 is :",t[:4])

# Q. 11 Create a tuple with mixed data types (int, float, string, boolean) and print it.
mixedtuple = ("Jayashri" , 45 , 4.5 , True )
print( "Mixed tuple is :",mixedtuple)

# Q. 12 Check whether Python exists in a given tuple and print the result.
newtuple = ("Math" , "Java" , "Python" , "css")
print("Python" in newtuple)

# Q.13 Convert a tuple to a list, add a new element, and print the updated list.
newtuple = ("Math" , "Java" , "Python" , "css")
print("tuple to a list conversion is :",list(newtuple))
newlist = list(newtuple)
newlist.append("HTML")
print("Upadated list is :", newlist)

# Q.14 Convert a list back into a tuple and print it.
newlist1 = ["Math" , "Java" , "Python" , "css" , "HTML"]
newsubtuple = tuple(newlist1)
print("Converted list to tuple is :" , newsubtuple)

# Q.15 Create two tuples and concatenate them using += operator.
tuple1 = (1,2,3,4)
tuple2= (10,20,30,40)
tuple1 += tuple2
print("Concatenated tuple is :" , tuple1)

# Q.16 Convert a tuple to list, change the second element, and convert back to tuple.
studenttuple = ("Jayashri" , "Anushka" , "Bhakti" , "Rinal" , "Khushi")
studentlist = list(studenttuple)
print("Converted tuple to list is :", studentlist)
studentlist[1] = "Komal"
updatedtuple = tuple(studentlist)
print("Updataed tuple is :" , updatedtuple)

# Q.17 Create a tuple and access elements using both positive and negative indexing.
stdtuple = ("Jayashri" , "Anushka" , "Bhakti" , "Rinal" , "Khushi")
print("access elements using positive indexing is :" , stdtuple[0])
print("access elements using positive indexing is :" , stdtuple[2])
print("access elements using negative indexing is :" , stdtuple[-1])
print("access elements using negative indexing is :" , stdtuple[-2])

# Q.18 Create a tuple of 7 elements and print its middle element.
numtuple1 = (10,20,30,40,50,60,70,80)
print("Middle element is :" , numtuple1[3])

# Q.19 Create a tuple and try to change one value directly (observe and write the error)
numtuple2 = (1,2,3,4,5)
numtuple2[2] = 10   
print(numtuple2)  # This will raise a TypeError: 'tuple' object does not support item assignment (because tuples are immutable/unchangeable).

# Q.20 Write a program that takes a tuple, converts it to list, replaces the last element, and converts back to tuple.
sampletuple = (100, 200, 300, 400, 500)
samplelist =  list(sampletuple)
samplelist[0] = 600
sampletuple2 = tuple(samplelist)
print("Updated tuple is :" , sampletuple2)

# Q.21 Create a tuple of 10 numbers and extract the middle 5 elements using slicing.
sampletuple3 = (1,2,3,4,5,6,7,8,9,10)
print(sampletuple3[2:7])

# Q.22 Write a program to check if a value exists in a tuple before accessing its index.
sampletuple4 = (10, 20, 30, 40, 50)
print(30 in sampletuple4)

# Q.23 Create a tuple, convert it to list, remove one item, and convert it back to tuple.
sampletuple5 = ("Jayashri", "Komal" , "Rajashri" , "Diksha" , "Sanika", "Supriya" , "Rutuja")
samplelist5 = list(sampletuple5)
samplelist5.remove("Jayashri")
sampletuple5 = tuple(samplelist5)
print("Converted back to tuple :" , sampletuple5)

# Q.24 Write a program that accepts a tuple, converts it to list, inserts a value at index 2, and converts back to tuple
sampletuple6 = (1,2,3,4,5)
samplelist6 = list(sampletuple6)
samplelist6.insert(2 , 10)
sampletuple6 = tuple(samplelist6)
print("Updated tuple is :" , sampletuple6)

# Q.25 Create a tuple and demonstrate slicing with positive and negative indexes in one program
sampletuple7 = (10,20,30,40,50,60,70,80,90)
print("slicing with positive indexing is :" , sampletuple7[2:6])
print("slicing with negative indexing is :" , sampletuple7[-7:-3])

# Q.26 Write a complete program that :-
# * creates a tuple
# * prints its length
# * accesses elements
# * slices it
# * converts to list
# * updates a value
# * converts back to tuple

tuple3 = (11,12,13,14,15,16,17,18,19,20)
print("Length of tuple is:" , len(tuple3))
print("Accessed Element using indexing is :" ,tuple3[3])
print("sliced elements are :" , tuple3[2:6])
list3 = list(tuple3)
print("Tuple converted into List is :" , list3 )
list3.insert(2,30)
tuple3 = tuple(list3)
print("Updated and converted into tuple :", tuple3)

#Q.27 Write a program that takes two tuples, adds them, and prints the final result
tuple4 = (1,2,3,4)
tuple5 = (10,20,30,40)
tuple4 += tuple5
print("Concatenated Tuple is :" , tuple4)
 
# Q.28 Create a tuple, delete it using del , and then try to print it (observe the error)

tuple6 = (1 ,10 ,100 ,1000 ,10000)
del tuple6
print(tuple6)   #This will raises a NameError: name 'tuple6' is not defined. because we already deleted a tuple6 using del keyword


# Q.29 A school stores a student’s basic details in a tuple because the data should not be changed accidentally.
#        The tuple contains: student = ("Rahul", 10, "A", 85.5)
#        Write a program to:
# 1. Print the student’s name and class using indexing.
# 2. Check whether "A" exists in the tuple.
# 3. Convert the tuple into a list, change the marks (85.5 → 90.0), and convert it back into a tuple.
# 4. Print the final updated tuple.

student = ("Rahul", 10, "A", 85.5)
print("Student Name :",student[0])
print("Class :",student[1])
print("A" in student)
newstudentlist = list(student)
newstudentlist[3] = 90.0
student = tuple(newstudentlist)
print("Final updated tuple is :" , student)

# Q.30 A customer’s selected product prices are stored in a tuple:
#       prices = (250, 500, 750, 1000, 1250)
#        Write a program to:
# 1. Print the total number of items using len().
# 2. Print the first and last price using positive and negative indexing.
# 3. Extract the middle three prices using slicing.
# 4. Convert the tuple into a list, add a new price 1500, and convert it back into a tuple.
# 5. Print the final tuple.

prices = (250, 500, 750, 1000, 1250)
print("Total number of items is :" , len(prices))
print("First price is :",prices[0])
print("Last price is :" , prices[-1])
print("Middle three prices is :", prices[1:4])
priceslist = list(prices)
priceslist.append(1500)
prices = tuple(priceslist)
print("Final tuple is :" , prices)