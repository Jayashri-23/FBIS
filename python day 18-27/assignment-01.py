# Variable to strore name
name = "Jayashri"
print("Name:" ,name)

# length of string
str = "Python"
print("Lenght of String is:", len(str))

#  print 1st character of "Karan"
str1 = "Karan"
print("The first charater is: ", str1[0])

# convert "Maharashtra" into uppercase
string = "Maharashtra"
print("In Uppercase:", string.upper())

# convert "Maharashtra" into lowercase
string1 = "Maharashtra"
print("Lowercase is:", string1.lower())

# Remove extra space from string
str2 = "      Hello python"
print("Remove extra space:", str2.strip())

# to check whether the "rashtr" is present in "Maharashtra"
string2 = "Maharashtra"
print("rashtr" in string2 )

# concatenate two str
a = "Hello"
b = "World!"
c = a + b
print("Concatenated String:", c)

# print each character of string using indexing
str3 = "india"
print(str3[0])
print(str3[1])
print(str3[2])
print(str3[3])
print(str3[4])

# print multiline string using triple quotes ''' '''
str4 = '''Hello  
Welcome to
FutureBright IT Solutions.'''
print(str4)

# print last character of "python"
str5 = "Python"
print("Last character is:", str5[-1])

# print first 4 character of "Maharashtra"
str6 = "Maharashtra"
print(str6[0:4])
print(str6[:4])

# print "Maharashtra" from index 3 till  the end
str6 = "Maharashtra"
print(str6[3:])

#  print characters of "Maharashtra" by skipping every second character
str7 = "Maharashtra"
print("Every second character of string is :" , str7[::2])

#  check whether "text" is not present in "Maharashtra"
str8 = "Maharashtra"
print("text" not in str8)


#  replace all occurrences of "a" with "A" in "Hello Maharashtra"
str9 = "Hello Maharashtra"
print("Replace by A :", str9.replace("a","A"))

#  split the string "Hello Maharashtra proud to be your son" into a list
str10 = "Hello Maharashtra proud to be your son"
print(str10.split())

#  reverse the string "Karan" using slicing
str11 = "Karan"
print("Reverse string is:" , str11[::-1])

#  print the middle character of the string "Python"
str12 = "Python"
print("Middle Character is:" , str12[3:4])

#  print the length of a string after removing extra spaces from both ends
str13 = "   Hello World   "
print("Len. of str after removing space: ", len(str13.strip()))

# reverse a string without using any inbuilt method (use slicing only).
str14 = "Hello World!"
print(str14[::-1])

#  count how many times the character "a" appears in "Maharashtra"
str15 = "Maharashtra"
print(str15.count("a"))

# program to extract "rashtr" from the string "Maharashtra" using slicing
str16 = "Maharashtra"
print(str16[4:10])

#  print the string "Maharashtra" in reverse order with step -1
print(str16[::-1])

# print alternate characters from the string "Programming"
str17 = "Programming"
print(str17[::2])

#  program to remove starting and ending spaces from the string "       Hello Maharashtra       "
str18 = "         Hello Maharashtra           "
print(str18.strip())

#  print characters from index -5 to -1 of the string "Maharashtra"
str16 = "Maharashtra"
print(str16[-5:-1])

#  print each word of the string "Python is very easy" on a new line.
print("Python \n is \n very \n easy")