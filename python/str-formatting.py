# # Take input from user
name = input("Enter your name:")
print(name)


# use of end parameter in print function (starts new line)
print("hello , welcome to FBIS",end="\n")
print("heello students")

# format() function in python  

# to put variable value in string we can use format() function
name = "jayashri"
age = 20
dob ="23/05/2006"
print("Hello {} , your age is {} and your date of birth is {}".format(name,age,dob) )

# # to put variable value in string we can use f-string
print(f"Hello {name} , i am  {age} year old and your date of birth is {dob}")