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
