#anaconda for pre-installed packages
#pip: which is a python package manager that allows you to easily install 3rd party packages
#iPython: much nicer python shell to work with. 
#anaconda comes with both

#(1) Whitespace Formatting:
#whitespace is ignored inside parentheses and brackets

#(2) Modules:
#certain features of Python aren't loaded by default so we use IMPORT to load the modules
#import re    to import regex
#import matplotlib.pyplot as plt       to import matplotlib

#(3) Functions:
#simply a rule for taking zero or more inputs and returning a corresponding output. Typically defined using DEF
def double(x):
  return x * 2

#we can also assign functions to variables and pass them into functions, just like other arguments:
def apply_to_one(f):
  '''calls the function f with 1 as its argument'''
  return f(1)

my_double = double    #refers to the previously defined function
x = apply_to_one(my_double)  # equals 2

#function parameters can also be assigned a default argument, which you only need to specify if you want a value other than the default:
def my_print(message = "my default message"):
  print message
  
my_print("hello")    # prints 'hello'
my_print()           # prints 'my default message'

# we can use a lamda here too, which is just a short anonymous function:
y = apply_to_one(lambda x: X + 4)  #equals 5

#(4) Exceptions:
#use these to manage things when they go wrong
# TRY and EXCEPT
try: 
  print(0/0)
except ZeroDivisionError:
  print("cannot divide by zero")
  
#(5) Lists:
integer_list = [1, 2, 3]
heterogenous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogenous_list, []]

#indexing:
x = range(10)   # is the list [0, 1, ...9]
zero = x[0]
one = x[1]
nine = x[-1]    # pythonic way of getting the last element from x 
eight = x[-2]   # pyhthonic way of getting next to last element from x

#slicing:
first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

#checking membership in a list:
1 in [1, 2, 3]   # True
0 in [1, 2, 3]   # False

#concat:
x = [1, 2, 3]
y = X + [4, 5, 6]

#append (more frequently used than concat):
x = [1, 2, 3]
x.append(0)    # x = [1, 2, 3, 0]

#(6) Tuples
#essentially immutable lists. you can do anything to a tuple that you can do to a list except modify it.
my_tuple =  (1, 2)

#tuples are a convenient way of returning multiple values from functions:
def sum_and_product(x, y):
    return (x+y), (x*y)
  
sp = sum_and_product(2,3)    #equals (5, 6)
s, p = sum_and_product(5, 10) # s equals 15, p equals 50

#(7) Dictionaries
#associates values with keys, allows you to quickly retrieve the value corresponding to the given key:

  empty_dict = {}
  grades = {"Trap": 100, "Mega": 90}
  traps_grades = grades["Trap"]   # to look up Trap's grades
  
  #check for existance of a key using in:
  trap_has_a_grade = "Trap" in grades    # True
  bradley_has_a_grade = "Bradley" in grades # False
  
  #dicts have a get method that returns a default value (instead of raising an exception) when you look up a key that's not in the dict:
  traps_grades = grades.get("Trap", 0)  # equals 100
  brads_grades = grades.get("Brad", 0)  # equals 0
  no_ones_grade = grades.get("No One")  # default is None
  
  #assigning key-value pairs, use []
  grades["Traps"] = 89    # replaces old value of 100
  grades["Hoang"] = 77    # adds a new entry for Hoang
  num_students = len(grades)    #equals 3
  
  #besides looking a specific keys, we can look at all of them:
  #.keys()   lists out all keys
  #.values() lists out all values
  #.items()  lists out all (key, value) tuples
  
  #defaultdict: is like a regular dictionary except that when you try to look up a key that it doesn't contain, it adds a value for it using a zero-argument function
  from collections import defaultdict
  
  word_counts = defaultdict(int)    #int() produces 0
  for word in document:
     word_counts[word] += 1
      
 
  


