# ------------------------------------------------ASCII
# NABIL BOUGHDAD, I HATE MY JOB


print("""
N     N      A      B B B B  I I I I I  L
N N   N    A   A    B      B     I      L
N  N  N  A A A A A  B B B B      I      L
N   N N  A       A  B      B     I      L
N     N  A       A  B B B B  I I I I I  L L L L L
""")

print("""
B B B B    O O O   U     U    G G G    H     H  D D D        A      D D D
B      B  O     O  U     U  G          H     H  D    D    A     A   D    D
B B B B   O     O  U     U  G     G G  H H H H  D     D  A A A A A  D     D
B      B  O     O  U     U  G      G   H     H  D    D   A       A  D    D
B B B B    O O O    U U U     G G G    H     H  D D D    A       A  D D D
""")


# ------------------------------------------------LOVESEATS

lovely_loveseat_description = """Lovely Loveseat. Tufted polyester
blend on wood. 32 inches high x 40
inches wide x 30 inches deep. Red or
white."""
lovely_loveseat_price = 254.00
stylish_settee_description = """Stylish Settee. Faux leather on
birch. 29.50 inches high x 54.75
inches wide x 28 inches deep. Black."""
stylish_settee_price = 180.50
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36
inches tall. Brown with cream shade."""
luxurious_lamp_price = 52.15
sales_tax = 0.088
customer_one_total = 0
customer_one_itemization = ""
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_itemization += "\n"+luxurious_lamp_description
customer_one_total += luxurious_lamp_price
customer_one_tax = customer_one_total*sales_tax


print("Customer One Items:\n"+customer_one_itemization)
# print("HT:"+str(customer_one_total))
customer_one_total += customer_one_tax
print("Customer One Total:\n"+str(customer_one_total))

# ------------------------------------------------CONTROL FLOW
# Boolean expresions are expression wich can be evaluated
# with True or False these last ones are boolean variables
# relational operators are == || != (Compare two items and return True or False)
bool1 = "True"
print(type(bool1))
bool2 = True
print(type(bool2))
# boolean types are fundamental for building conditional statements
# Example of a controlflow
user_name = "angela_catlady_87"
# user_name = "Dave"
if user_name == "Dave":
    print("Get off my computer Dave!")
elif user_name == "angela_catlady_87":
    print("I know it is you, Dave! Go away!")
# relational operators are > >= < <=
# Boolean operators are 'and' 'or' 'not' last operator reverses boolean value
# ------------------------------------------------ERRORS
# Syntax Error: means there is something wrong the way your program is written
# mostly misspelling keyword, paranthesis , semicolumns etc...
# Name Error: common error is misspelling or forgetting ...
# Type Error: the attempts to use an operator on something of the incorrect type
# Logic errors: Errors found by the programmer when the program isn’t doing
# what it is intending to do.
# ------------------------------------------------LISTS AND TUPLES
# lists in python can store every variable type
# lists Methods
orders = ["daisies", "periwinkle"]
print(orders)
orders.append('tulips')
ordersNew = orders+['jasmin', 'roses']
print(ordersNew)
# lists can be concatenated with + however it has to be a list also
# there are so many useful methods for the lists .insert();.pop();.remove()
# .count();.append();.clear();.index();.sort() etc..
# the function range() is important it is used to create series of succeding numbers
# len() is used to measure the length of a list
# we can slice a list by assigning it to a variable likewise 'l2=l1[1:4]' l1 is a list bear in mind index 4 isn't included
# slicing can even be done likewise [:n] or [-n:] or [:-n]
# .sort() used in a descending order can be used in ascending with the parameter (reverse=True)
# sorted(l1) can assign the sorted "l1" to a new list with sorted order unlike .sort() wich returns no value
# tupples are lists but they're "immutable" can't be changed reassigned
# tup1=("Nabil",31,"pilot") how ever you can attribute tupple values to variables likewise
# name,age,work=tup1 to create a one element tupple you have to put trailing comma tup2=(5,)
# we can join two lists in one with the following method zip(l1,l2) values will be joined as a tupple and
# the variable storing the zip has to be converted to a list with the following method .list(l3)
# ------------------------------------------------LOOPS
# this is an example of a foor loop
# for <temporary variable> in <collection>:
#   <action>
# you ought to make  your temporary variable descriptive to distinguish it from other variables
# While loop needs a variable and it is required to get iterated
# while <conditional statement>:
#   <action>
python_topics = ["variables", "control flow", "loops", "modules", "classes"]
length = len(python_topics)
index = 0
while index < length:
    print("I am learning about "+python_topics[index])
    index += 1
# we must avoid infinite loops
# break and continue are useful tools to control a loop they're usually paired with if/elif/else statements
# nested loops are required in certain situations lists inside  lists or whatever
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]  # check below
# we can also put a conditional after the for loop above
# Example
# scaled_grades = [grade + 10 if grade > 70 else grade for grade in grades]
# is the same as
# scaled_grades = []
# for grade in grades:
#     scaled_grades.append(grade + 10)
print(scaled_grades)
# ------------------------------------------------FUNCTIONS
# Functions are a convenient way to group our code into reusable blocks.
# we can define a function likewise
# def foo():
#     <actions>
# functions admits parameters they should be stated in the paranthesis following the header
# there are 3 types of arguments (positional,keyword,default)
# positional parameters values should be called in order
# keyword parameters values can be called using the keyword ex

# def foo(x, y, z=1): # z is a default argument set to 1 we can omit giving value to z if calling foo
#     print(x/y)


# foo(y=1, x=2) #These are keywords arguments
# there are a lot of built-in python functions check them on the documentation for more
# info for example there is max();min();round(); print(); len() etc....
# to make a function useful it has to return a value we can return several values by separating them
# with commas example: return a,b,c
# def top_tourist_locations_italy():
#     first = "Rome"
#     second = "Venice"
#     third = "Florence"
#     return first, second, third


# top_tourist_locations_italy() = most_popular1, most_popular2, most_popular3
# print(most_popular1)
# print(most_popular2)
# print(most_popular3)
# ------------------------------------------------SCOPE
# The scope of our data(Variables etc....) is the level at which it can be accessed.
# Global scope means declaring a variable that can be accessed in the whole Program
# Local scope means the variables that are found within a function
def lots_of_math(a, b, c, d):
    print(a+b)
    print(c-d)
    print((a+b)*(c-d))
    return ((a+b)*(c-d)) % a


love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ',
                    'you lay down your arms', '           like flowering mines    ', '\n', '   to conquer me home.    ']

love_maybe_lines_stripped = []
for item in love_maybe_lines:
    love_maybe_lines_stripped.append(item.strip())
# print(love_maybe_lines_stripped)
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

# ------------------------------------------------MODULES
# modules are a collection of reusable code can be called above your program to make use of it, they re often refered to as "Packages" or "libraries"
# example of a library or a module is datetime we use "from datetime import datetime" in order to invoke the module datetime
# there is also the module "random"
# check the documentation for more modules
# ---------(NAMESPACE)-------------------------------------
# the namespace is the distinction between your main.py and the code you want to run abroad your file example: "import random" random is a namespace
# sometimes the namespace can be long or very ambiguous we can use the acronym 'as' example "import datetime as dt" see now the namespace becomes "dt" only
# we might also import a module as a wildcard and every function or variable in it can be called within the code with just the name you don't have to state the
# module each time you want to use it example "from datetime import *" some applications of modules and namespace
# from matplotlib import pyplot as plt
# import random
# # Add your code below:
# numbers_a = range(1,13)
# numbers_b = random.sample(range(1000),12)
# plt.plot(numbers_a,numbers_b)
# plt.show()
# ------------------------------------------------PIPENV
# it is used to work on a specific version of python or a specific version of a library in python it is set up on my computer however specifying
# the version require some bash commands inside the concerned project example 'pipenv --three' means this project will run python3 to install
# a py library we use the command "pip install numpy" if you want to install a specific version use the same command but likewise "pipenv install numpy==1.15.4"
# to access the project that has the specified versions we use "pipenv shell"
# ------------------------------------------------DICTIONARIES
# a dictionary is an unordered type of data which has keys with a corresponding values "KEY":"VALUE"
# car={"make":"Mercedes","model":"C-Class","year":2022} this is an example of a dictionary
# we can't have a list a keys however we can have values as lists. the reason is the keys must be static unchangeable to add a value to the dictionnary
# we use example : car["fuel"]="diesel" this should add the "fuel":"diesel" to the car dictionary this way is used to overwrite a value also
# if we want to use multiple Key:value to a dictionary we use car.update({key: value, key: value, key: value})
# we can create a dictionary by combining two lists likewise :
# names = ['Jenny', 'Alexus', 'Sam', 'Grace']
# heights = [61, 70, 67, 64]
# students = {key: value for key, value in zip(names, heights)}
# or we can do it likewise
# students = dict(zip(names, heights))
# print(students)
# we can use try/except if the key doesn't exist in the dictionary in order to avoid a KeyError
# the dictionary has a method to get the value of key safe if it doesn't exist it will throw a None value instead of an Error you can even
# state the value if the key doesn't exist by adding it as a second argument example dictionary.get("key",0) now to remove a key we use
# and return a value if the key isn't found .pop("key","value") the function list(dictionary) will list all the keys of a dictionary
# and the method dictionary.keys() will also list the keys of the dictionary but it can't be modified if you did attribute it to a variable
# you can get the(key, value) set with the method .items() you can iterate through and dictionary  like wise
# for key,value in dict.items():
# Do something with key and value
# ------------------------------------------------  CLASSES AND OBJECTS
# object oriented programming is a way of programming it gives the programmer the freedom to model new data types example: a car
# it can have(model, year, type etc we call these "attributes" the modeled data type has functionalities fly(), swim() etc... we call them "methods")
# classes have always the first letter capitalized; attributes can either be strings, ints,floats,booleans even objects
# example of a class
# class Dog:
#       # To create a Dog, give it a name, breed, and age. age is in years.
#   # If you don't give an age, we'll say it's 0 years old (a puppy).
#   # All dogs also start as friendly!
# __init__ is a constructor function
#   def __init__(self, input_name, input_breed, input_age = 0, input_friendliness = True):
#     # self.name is this specific dog's name
#     self.name = input_name
#     self.breed = input_breed
#     self.age = input_age
#     self.is_friendly = input_friendliness

# Create a __repr__ method it is a method that returns a full description of a Class items
# def __repr__(self):
#   description = f"{self.name} is a {self.breed}, he/she is {self.age}, "
#    if self.is_cuddly == True:
#         description += f"{self.name} is a cuddly cat"
#     else:
#         description += f"what a bad cat!"
#     return description
