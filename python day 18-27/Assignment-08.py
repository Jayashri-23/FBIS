
# Assignment - 08

# Q.1 Create a dictionary with keys name, rollNo, and address and print it.
student_dict = {
    "name": "Jayashri",
    "rollno" : 20,
    "address":"Nashik"
}
print(student_dict)

# Q.2 Write a program to access and print the value of key name from a dictionary
print(student_dict["name"])

# Q.3 Create a dictionary and print its length using len().
student = {
    "name" : "Jayashri",
    "rollno" :15,
    "address": "Nashik",
    "id" : 101
}
print(len(student))

# Q.4 Write a program to check the type of a dictionary using type()

print(type(student))

# Q.5 Create a dictionary with two keys and print all its values
data = {
    "name" : "Jayashri",
    "rollno" : 15,
}
print(data.values())

# Q. 6 Create a dictionary and access values using both [] and get() methods.
stud_data = {
    "name": "jayashri",
    "rollno" : 15 ,
    "address" : "Nashik" ,
    "id" : 101
}
print(stud_data["address"])       # Using [] method

print(stud_data.get("name"))      # Using get() method

#  Q.7 Write a program to add a new key-value pair to an existing dictionary.
stud_data["email"] = "jayashrigodge@gmail.com"
print(stud_data)

# Q.8 Create a dictionary and update one value using the update() method.
stud_info = {
    "name" : "Jayashri",
    "rollno" : 15,
    "address" :"Nashik",
    "State" : "Maharashtra",
    "Country" : "India"
}
stud_info.update({"address" : "Pune"})
print(stud_info)

# Q.9 Write a program to remove a key using the pop() method
stud_info.pop("rollno")
print(stud_info)

# Q.10 Create a dictionary and remove the last inserted item using popitem().
stud_info.popitem()
print(stud_info)

# Q.11 Write a program to print all keys using the keys() method
print(stud_info.keys())

# Q.12 Write a program to print all values using the values() method
print(stud_info.values())

# Q.13 Create a dictionary and print all key-value pairs using items()
print(stud_info.items())

# Q.14 Convert a tuple of key-value pairs into a dictionary using dict()
tuple_data = (("name","Jayashri"), ("rollno",15),("address", "Nashik"),("state", "Maharashtra"))
tupletodict = dict(tuple_data)
print(tupletodict)

# Q.15 Write a program to check if a key exists in a dictionary
print("name" in stud_info)

# Q.16 Create a dictionary with duplicate keys and print the output
studdata = {
    "name" : "Jayashri",
    "rollno" : 15,
    "address" : "Nashik",
    "name" : "Khushi"
}
print(studdata)

# Q.17 Write a program to delete a specific key using the del keyword
del studdata["address"]
print(studdata)

# Q.18 Write a program to delete the entire dictionary using del.
del studdata
# print(studdata)  # This will raise an error as studdata is deleted

# Q.19 Create a dictionary and empty it using the clear() method
studinfo = {
    "name" : "Jayashri",
    "rollno" : 15,
    "address" : "Nashik"
}
studinfo.clear()
print(studinfo)

# Q.20 Copy a dictionary using the copy() method and show both dictionaries
originaldict = {
    "name" : "Jayashri",
    "rollno" : 15,
    "address" : "Nashik"
}
copieddict = originaldict.copy()
print("Original Dictionary :", originaldict)
print("Copied Dictionary :", copieddict)

# Q.21 Copy a dictionary using the dict() constructor and modify the original dictionary.
originaldict1 = {
    "name" : "Jayashri",
    "rollno" : 15,
    "address" : "Nashik"
}
copieddict1 = dict(originaldict1)
originaldict1["address"] = "pune"
print("Original Dictionary :", originaldict1)
print("Copied Dictionary :", copieddict1)

# Q.22 Write a program to demonstrate why dict1 = dict2 is not a proper copy.
dict1 = {
    "name" : "Jayashri",
    "rollno" : 15,
    "address" : "Nashik"
}
dict2 = dict1                                 # Not a proper copy (Reference)
dict2["address"] = "pune"
print("Original Dictionary :", dict1)
print("Copied Dictionary :", dict2)

# Q.23 Create a dictionary and add multiple items using assignments
student1 = {
    "name" : "Jayashri",
    "rollno" : 15,
    "address" : "Nashik"
}
student1["email"] = "jayashrigodge@gmail.com"
student1["state"] = "Maharashtra"
print(student1)

# Q.24 Write a program to remove multiple keys one by one using pop()

student1.pop("email")
student1.pop("state")
print("Dictionary after removing multiple keys :",student1)

# Q.25 Use fromkeys() to create a dictionary with default values
datadict = dict.fromkeys(["name","rollno","address"])
print(datadict)


# Q.26 Write a program to access a missing key using get() without error.
data1 = {
    "name" : "Jayashri",
    "rollno" : 15,
    "address" : "Nashik"
}
print(data1.get("email"))

# Q.27 Create a dictionary and print key-value pairs in tuple form
data2 = {
    "name" : "jayashri",
    "rollno" :15,
    "address" : "Nashik",
    "state" : "Maharashtra",
    "country" : "India"
}
tupledata = tuple(data2.items())
print(tupledata)


# Q.28 Write a program to update multiple values using update()
data3 = {
    "name" : "Jayashri",
    "rollno" : 15,
    "address" : "Nashik"
}
data3.update({"address" : "Pune" , "rollno" : 20})
print(data3)

# Q.29 Create a dictionary and check membership of a key using in
data4 = {
    "name" : "Jayashri",
    "rollno" : 15,
    "address" : "Nashik"
}
print("rollno" in data4)

# Q.30 Write a program that creates a dictionary from tuples and accesses values using keys.
tupledata1 = (("name","jayashri"), ("rollno",15),("address", "Nashik"),("state", "Maharashtra"))
tupletodict1 = dict(tupledata1)
print(tupletodict1)
print(tupletodict1["state"])