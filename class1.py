# for Single Line Comment ctrl slash
""" For multi line comment ctrl shift slash """

name = "Bishal" # we don't put string in single quote because it is a dynamic typed language
age = 12 # age is an integer variable
location = "Kathmandu" # location is a string variable
#concat
print("My name is " + name + " and my age is " + str(age) + " and I live in " + location) # we have to convert integer to string because we can't concat string with integer

#f String
print(f"My name is {name} and my age is {age} and I live in {location}") # we can use f string to concat string with integer without converting it to string

#format old version
print("My name is %s and my age is %d and I live in %s" % (name, age, location)) # we can use format old version to concat string with integer without converting it to string


#format new version
print("My name is {} and my age is {} and I live in {}".format(name, age, location)) # we can use format new version to concat string with integer without converting it to string

print(type(name)) # we can use type() function to check the data type of a variable

name = input("Enter your name: ") # we can use input() function to take input from user
age = int(input("Enter your age: ")) # we can use int() function to convert string to integer
location = input("Enter your location: ") # we can use input() function to take input from user

#concat
print("My name is " + name + " and my age is " + str(age) + " and I live in " + location) # we have to convert integer to string because we can't concat string with integer

#f String
print(f"My name is {name} and my age is {age} and I live in {location}") # we can use f string to concat string with integer without converting it to string

#format old version
print("My name is %s and my age is %d and I live in %s" % (name, age, location)) # we can use format old version to concat string with integer without converting it to string


#format new version
print("My name is {} and my age is {} and I live in {}".format(name, age, location)) # we can use format new version to concat string with integer without converting it to string

print(type(name)) # we can use type() function to check the data type of a variable

