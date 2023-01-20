# # Defining variable
# name ="Beau"
# # age=39
# # Expressions and statements
# print(name)

# # Comments : Can be inline

# #Data type
# print(type(name)) #Check datatype

# #checking data type
# if(isinstance(name,str) == True):
#   print(f"{name} variable provided is a String")

# age = float(2) #Conversion using class constructor
# print (isinstance(age, int))


# Operators

# age = 8 #Assignment operators
# age += 8 #Age 8+8
# print(age)

#Boolean Operators
#or prints true value
# print(0 or 1)

# print("simon" and 1)

# def is_Adult():
#   age = input("Input your age: ")
#   if age>18:
#     return True
#   else:
#     return "You are young"

# is_Adult()

# name = "Simon"

# print(name.lower())
# print("in" in name)

#Finding characters
# name = "si\"mon"
# print(name[1:])

# done = ""

# if done:
#   print("yes")
# else:
#   print("no")

#Number Data Types

# num = 3 + 3j

# num2 = complex(2,3)

# print(num + num2)

#Enums

# from enum import Enum 

# class State(Enum):
#   INACTIVE =0
#   ACTIVE =1
# print(list(State))

#inputs
# age = input("What is your age")
# print(f"your age is {age}")


#lists
# dogs = ["ROger",1, "Syd", True]

# print("Roger" in dogs) #Check if value exists
# print(dogs[2]) #Retrieve item

# print(len(dogs)) #check number of items

#Append list

# dogs.append("Simon") ##Add to the list
# print(dogs)

#Add items in a specific index
# dogs.insert(2,"test")


# dogs[1:1] = ["test1", "test 2"]
# print(dogs)

#Tuples
#Allowed to create immutable objects(which you can't change once added)

# names= ("Roger", "Syd")

# names[0]
# names.index("Roger")

# len(names)
# print("Roger" in names)
# print(sorted(names))


#Dictionaries

# dog = {"name" :"Roger", "age":8, "color":"green"}

# print(dog.get("color","brown"))

# print(dog.popitem()) #remove the last item in dictionary
# print(dog)

# print(dog.keys())
# print(list(dog.items())) #Print dictionary items in a list format 
# dog["favorite food"] = "meat" #Add item in dictionary
# print(dog)


#Sets
#They look like dictionary, are mutable , and don't have keys

# set1 = {"Roger", "Syd"}
# set2 = {"Roger"}
# Intersect two sets
# intersect = set1 & set2 #prints the common data
# print(intersect)

#mod
# set2 = {"Luna"}
# mod = set1 | set2 
# print(mod)

# mod = set1 < set2 #Check if item is superset of another
# print(mod)

# NB: set cannot have two of the same item


# print(list(set1))#Convert set into list

#FUNCTIONS 

# #Calling a basic fxn
# def Hello():
#   print ("Hello!")

#Add variable
# def Hello(name):
#   print ("Hello " + name)

# Hello("Simon")
# Hello("Peter")

#Parameters - values accepted by function inside fnx definition
#args - values passed to the fnxn when we call it

# Pass Default argument when there is no other value passed
# def hello(name="Peter"):
#   print('Hello ' + name )

# hello()


#Fnxn can return a value using return statement
# def hello(name):
#   if not name:
#     return  #return is used as a default to end a function if condition is not met
#     print('Hello'+name+'!')


#Variable Scope

#there are Global and private variables in a function

# age = 8 #Global var- can be called by any function

# def test():
#   age=9  #private variables have ability to modify global vars
#   print(age)
# test()


#Functions can be nested inside other functions

# def talk(phrase):
#   def say(word): #Nested function only viscible inside a function
#     print(word)
#   words = phrase.split(' ')
#   for word in words:
#     say(word)
# talk('I am going to buy the milk')

#changing local variables into global feature

# def count():
#   count = 0
#   def increment():
#     nonlocal count #Made local variable to global
#     count = count + 1
#     print(count)
#   increment()

# count()

#closures 

# def counter():
#   count = 0
#   def increment():
#     nonlocal count
#     count = count +1
#     return count
#   return increment 
# increment = counter()
# print(increment()) #1
# print(increment()) #2
# print(increment()) #3

#Object
#have attributes and methods

# age = 8

# print(age.real) #8
# print(age.imag) #0 because no imaginary value set
# print(age.bit_length())

#some objects are immutable others are mutable

#Loops
#two types - 1. for ... 2. while ...

#while loops
#run a function until a condition is false
# count = 0
# while count < 10: #run for 10 times
#   print("Condition is True")
#   count = count + 1
# print("After the loop")