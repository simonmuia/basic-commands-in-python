# # Defining variable
"""
name ="Beau"
# age=39
# Expressions and statements
print(name)
"""

# # Comments : Can be inline

## Data type
# print(type(name)) #Check datatype

# #checking data type

"""
if(isinstance(name,str) == True):
  print(f"{name} variable provided is a String")

age = float(2) #Conversion using class constructor
print (isinstance(age, int))
"""

# Operators
"""
age = 8 #Assignment operators
age += 8 #Age 8+8
print(age)

"""


#Boolean Operators
#or prints true value
# print(0 or 1)

# print("simon" and 1)
"""
def is_Adult():
  age = input("Input your age: ")
  if age>18:
    return True
  else:
    return "You are young"

is_Adult()

"""

"""
name = "Simon"

print(name.lower())
print("in" in name)

"""


#Finding characters

# name = "si\"mon"
# print(name[1:])


"""
  done = ""

if done:
  print("yes")
else:
  print("no")
  
"""

#Number Data Types
"""
num = 3 + 3j
num2 = complex(2,3)
print(num + num2)

"""


#Enums

# from enum import Enum 
"""

class State(Enum):
  INACTIVE =0
  ACTIVE =1
print(list(State))

"""


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


"""

dog = {"name" :"Roger", "age":8, "color":"green"}

print(dog.get("color","brown"))

print(dog.popitem()) #remove the last item in dictionary
print(dog)

"""

# print(dog.keys())
# print(list(dog.items())) #Print dictionary items in a list format 
# dog["favorite food"] = "meat" #Add item in dictionary
# print(dog)


#Sets
#They look like dictionary, are mutable , and don't have keys

"""

set1 = {"Roger", "Syd"}
set2 = {"Roger"}
Intersect two sets
intersect = set1 & set2 #prints the common data
print(intersect)

"""


#mod
"""
set2 = {"Luna"}
mod = set1 | set2 
print(mod)

mod = set1 < set2 #Check if item is superset of another
print(mod)
"""



# NB: set cannot have two of the same item


# print(list(set1))#Convert set into list

#FUNCTIONS 

# #Calling a basic fxn
"""
def Hello():
  print ("Hello!")
  
  """

#Add variable
# def Hello(name):
#   print ("Hello " + name)

# Hello("Simon")
# Hello("Peter")

#Parameters - values accepted by function inside fnx definition
#args - values passed to the fnxn when we call it

# Pass Default argument when there is no other value passed
"""
def hello(name="Peter"):
  print('Hello ' + name )

hello()
"""



#Fnxn can return a value using return statement

"""
def hello(name):
  if not name:
    return  #return is used as a default to end a function if condition is not met
    print('Hello'+name+'!')
"""

#Variable Scope

#there are Global and private variables in a function


"""

age = 8 #Global var- can be called by any function

def test():
  age=9  #private variables have ability to modify global vars
  print(age)
test()
"""


#Functions can be nested inside other functions
"""
def talk(phrase):
  def say(word): #Nested function only viscible inside a function
    print(word)
  words = phrase.split(' ')
  for word in words:
    say(word)
talk('I am going to buy the milk')

"""


#changing local variables into global feature

"""
def count():
  count = 0
  def increment():
    nonlocal count #Made local variable to global
    count = count + 1
    print(count)
  increment()

count()

"""


#closures 

"""
def counter():
  count = 0
  def increment():
    nonlocal count
    count = count +1
    return count
  return increment 
increment = counter()
print(increment()) #1
print(increment()) #2
print(increment()) #3
"""

#Object
#have attributes and methods
"""
age = 8

print(age.real) #8
print(age.imag) #0 because no imaginary value set
print(age.bit_length())
"""

#some objects are immutable others are mutable

#Loops
#two types - 1. for ... 2. while ...

#while loops
#run a function until a condition is false
"""
  count = 0
while count < 10: #run for 10 times
  print("Condition is True")
  count +=
print("After the loop")

items = [1, 2, 3, 4]
Basic for loop

for item in items:
  print(item)
"""

#get range of numbers

# for item in range(15):
#   print(item)


#items = ["simon", "peter", "mark", "doe"]
#get index of items
# for index, item in enumerate(items):
#   print(index, item) #prints items alongside their indexes

#continue - stops current iteration
#break - stops the loop all together

"""
items = [1,2,3,4]

for item in range(15):
  if item == 2:
    continue  #skip num 2 
  elif item == 10:
    break #stop the loop
  print(item)
"""
  
  
#Classes 

#Object is an instance of a class, class is a type of object
"""
class Dog:
  def bark(self):
    print("woof!")
roger = Dog()

print(type(roger)) #check type of object

print(roger)
"""


#Using Constructors 

"""
class Dog:
  def __init__(self,name,age): #type of constructors
    self.name = name
    self.age = age
  def bark(self):
    print("woof!")
    
roger = Dog("Roger", 8)

print(roger.name)
print(roger.age)
roger.bark()

"""


#Class Inheritance'

"""
class Animal:
  def walk(self):
    print("Walking...")
    
class Dog(Animal): #inherit from animal class
  def __init__(self,name,age): #type of constructors
    self.name = name
    self.age = age
  def bark(self):
    print("woof!")
    
roger = Dog("Roger", 8)

print(roger.name)
print(roger.age)
roger.walk()
roger.bark()

"""



#Modules 
#Every python file is a module
# Basic import
# from dog import bark #import a function from a file
# bark()

#import from a subfolder
# When importing a function in file located in a specific subfolder,
#You create file called __init__.py to enable imports accessible from files in that subfolder

# from lib.dog import bark
# bark()

#importing python standard libraries
#lets import math module

#basic import
"""
import math
squareRoot = math.sqrt(4)
print(squareRoot)
"""


#import specific function in the library
#e.g sqrt function

"""
from  math import sqrt

print(sqrt(4))
"""

#Accepting Arguments from command line
#by using sys module
# import sys
# print(sys.argv)

#example of command

# As many arguments as possible
#e.g. run python.py arg1 arg2
#then run python main.py simon 39
#prints ['main.py', 'simon', '39']

#Example 2


"""

import sys

name = sys.argv[1]
print("Hello " + name) 
Run python main.py simon
prints "Hello simon"

"""

#Example 3 - another way to pass args
#import argparse library
"""
import argparse

parser = argparse.ArgumentParser(
  description = "This program prints the name of my dogs"
)

#add args you want to accept
parser.add_argument('-c', '--color', metavar='color', required=True, choices={"red", "yellow"}, help='the color to search for')

args = parser.parse_args()
print(args.color)

#run command "python -c main.py -c red" example
#prints "red"
"""

# Lambda Functions
# Example
"""Lambda -> An anonymous inline function consisting of a single expression which is evaluated when the function is called. The syntax to create a lambda function is lambda [parameters]: expression"""
"""
lambda num : num * 2

multiply = lambda a,b : a*b

print(multiply(2,4))"""


#map() , filter() , reduce()
# Map function - map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

#Syntax - map(fun, iter) #fun - It is a function to which map passes each element of given iterable. #iter - It is a iterable which is to be mapped.

#Given the following list of items, map each to a list of its double:
"""numbers = [1,2,3]
#define function to double the iterables 
def double(a):
  return a*2

#1. Map() 
result = map(double, numbers)
print(list(result)) #print results"""

#use lambda function to solve above example
"""
numbers = [1,2,3]
#define lambda function to double the iterables 
double = lambda a : a*2

#1. Map() 
result = map(double, numbers)
print(list(result)) #print results"""

#2.FILTER()

"""
* The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

* 
filter(function, sequence)
Parameters:
function: function that tests if each element of a 
sequence true or not.
sequence: sequence which needs to be filtered, it can 
be sets, lists, tuples, or containers of any iterators.
Returns:
returns an iterator that is already filtered.
"""
#Example
#from the following list of items, print even numbers to a list
"""numbers=[1,2,3]

def isEven(n):
  return n%2 == 0 #Returns True

result = filter(isEven, numbers)

print(list(result))"""


#use lambda fnxs
"""numbers =[1,2,3,4]

isEven = lambda n: n%2==0

result = filter(isEven,numbers)
print(list(result))"""

#3. REDUCE()

"""
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
"""

#Example function without reduce function
#Calculate total expenses of items in the list of expeses

"""expenses = [
  ('Dinner', 80),
  ('Car', 120)
]
sum = 0
for expense in expenses:
  sum+=expense[1]

print(sum)"""
#example use of lambda function to render same solution
#import reduce function from functools standard library 
"""from functools import reduce

expenses = [
  ('Dinner', 80),
  ('Car', 120)
]
#lambda picks the items in the list, adds all second subitems
sum = reduce(lambda a,b: a[1]+b[1], expenses)

print(sum)"""

#Recurssion

#recursion - ability of function to call itself

#example
"""
def factorial(n):
  if n==1:return 1
  return n * factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))"""

#Decorators
"""
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. 

SYNTAX FOR DECORATORS

@gfg_decorator
def hello_decorator():
    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)'''

"""

#example
#Decorator - function that takes another function as parameter, wraps it as inner function and performs the job it has to do and returns it in a function

"""def logtime(func):
  def wrapper():
    #do something before
    print("Before")
    val = func()
    #do something after
    print("After")
    return val
  return wrapper
@logtime
def hello():
  print("Hello")

hello()"""

#These functions can be used in loggin, test performance, perform caching, verify informations etc

#DOCSTRINGS

"""
Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods.

It’s specified in source code that is used, like a comment, to document a specific segment of code. Unlike conventional source code comments, the docstring should describe what the function does, not how

What should a docstring look like?

The doc string line should begin with a capital letter and end with a period.
The first line should be a short description.
If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description.
The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.
Declaring Docstrings: The docstrings are declared using ”’triple single quotes”’ or “””triple double quotes””” just below the class, method or function declaration. All functions should have a docstring.

Accessing Docstrings: The docstrings can be accessed using the __doc__ method of the object or using the help function.
The below examples demonstrates how to declare and access a docstring.

"""
#Example

# def my_function():
#     '''Demonstrates triple double quotes
#     docstrings and does nothing really.'''
   
#     return None
  
# print("Using __doc__:")
# print(my_function.__doc__)
  
# print("Using help:")
# help(my_function)

#Output
"""Using __doc__:
Demonstrates triple double quotes
    docstrings and does nothing really.
Using help:
Help on function my_function in module __main__:

my_function()
    Demonstrates triple double quotes
    docstrings and does nothing really."""

#Annotations
"""
Function annotations are arbitrary python expressions that are associated with various part of functions. These expressions are evaluated at compile time and have no life in python’s runtime environment. Python does not attach any meaning to these annotations. 
"""
#Create a function to accept int only

"""
def increment(n: int) -> int:
  return n+1;
count: int = 0

"""

#Python Exception Handling

"""
Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program. 

Difference between Syntax Error and Exceptions

Syntax Error: As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of the program. 

#Example 

# initialize the amount variable
amount = 10000
  
# check that You are eligible to
#  purchase Dsa Self Paced or not
if(amount > 2999)
print("You are eligible to purchase Dsa Self Paced")

Output:
Syntax Error: Invalid Syntax


Exceptions: Exceptions are raised when the program is syntactically correct, but the code resulted in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program.

#Example

# initialize the amount variable
marks = 10000
  
# perform division with 0
a = marks / 0
print(a)

Output:
ZeroDivisionError: division by zero
"""

#Using try and Except statement

"""
Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause.

Example: Let us try to access the array element whose index is out of bound and handle the corresponding exception.

# Python program to handle simple runtime error
#Python 3
  
a = [1, 2, 3]
try: 
    print ("Second element = %d" %(a[1]))
  
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
  
except:
    print ("An error occurred")




# Output
Second element = 2
An error occurred


Catching Specific Exception

A try statement can have more than one except clause, to specify handlers for different exceptions. Please note that at most one handler will be executed. For example, we can add IndexError in the above code. The general syntax for adding specific exceptions are – 

try:
    # statement(s)
except IndexError:
    # statement(s)
except ValueError:
    # statement(s)

"""
#Example - using NameError and ZeroDivisionError for except statement

# Program to handle multiple errors with one
# except statement
# Python 3
  
"""def fun(a):
    if a < 4:
  
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
  
    # throws NameError if a >= 4
    print("Value of b = ", b)
      
try:
    fun(3)
    fun(5)
  
# note that braces () are necessary here for 
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")"""


# Output
# ZeroDivisionError Occurred and Handled
# If you comment on the line fun(3), the output will be 

# NameError Occurred and Handled

#Try with Else Clause
"""In python, you can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.

Example: Try with else clause
"""

"""
# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
  
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

"""

# Output:

# -5.0
# a/b result in 0 

"""Finally Keyword in Python
Python provides a keyword FINALLY, which is always executed after the try and except blocks. The final block always executes after normal termination of try block or after try block terminates due to some exception."""

#Example:
#  Syntax:

# try:
#     # Some Code.... 

# except:
#     # optional block
#     # Handling of exception (if required)

# else:
#     # execute if no exception

# finally:
#     # Some code .....(always executed)


# Python program to demonstrate finally
  
"""# No exception Exception raised in try block
try:
    k = 5//0  # raises divide by zero exception.
    print(k)
  
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
  
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')"""

# Output:

# Can't divide by zero
# This is always executed
"""
Raising Exception
The raise statement allows the programmer to force a specific exception to occur. The sole argument in raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from Exception)."""


# Program to depict Raising Exception
  
# try: 
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print ("An exception")
#     raise  # To determine whether the exception was raised or not

"""

OUTPUT: 
Traceback (most recent call last):
  File "/home/d6ec14ca595b97bff8d8034bbf212a9f.py", line 5, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there"""

"""# Example 2

class DogNotFoundException(Exception):
  print("Inside")
  pass
try:
  raise DogNotFoundException()
except DogNotFoundException:
  print("Dog Not Found!")
"""

#PIP 
"""
What is a pip?
Python pip is the package manager for Python packages. We can use pip to install packages that do not come with Python. The basic syntax of pip commands in command prompt is:

Python pip comes pre-installed on 3.4 or older versions of Python. To check whether pip is installed or not type the below command in the terminal.

Specifying Package Version
We can also install the package of a specific version by using the below command.

Syntax: 

pip install package_name==version

"""


#List Compression
#They operate sort of kinda loop

# numbers = [1,2,3,4,5]

# numbers_power_2 = [n*2 for n in numbers]

# print(numbers_power_2)

# number_power_2 = []
"""
for n in numbers:
  number_power_2.append(n**2)

print(number_power_2)
"""

#Using lambda
"""numbers_power_2 = list(map(lambda n : n**2, numbers))

print(numbers_power_2)"""

#POLYMORPHISM
"""
What is Polymorphism: The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.
"""

#Example

# class Dog:
#   def eat(self):
#     print("Eating dog food")

# class Cat:
#   def eat(self):
#     print('Eating cat food')

# animal1 = Dog()
# animal2 = Cat()

# animal1.eat()
# animal2.eat()


#OPERATOR OVERLOADING
"""
Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because ‘+’ operator is overloaded by int class and str class. You might have noticed that the same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading. """

#Example
"""
class Dog:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def __gt__(self,other):
    return True if self.age > other.age else False
roger = Dog('Roger', 8)
syd = Dog('Syd', 7)

print(roger>syd)"""