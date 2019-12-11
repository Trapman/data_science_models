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
      
  #counter: turns a sequence of values into a defaultdict(int)-like object mapping keys to counts. Primarily used for creating histograms
  
  from collections import Counter
  c = Counter([0, 1, 2, 0)]  # c is (basically) { 0:2, 1:1, 2:1}
  
  #gives us a clean way of doing a word count for instance:
              word_counts = Counter(document)
              
  #Counter has a most_common method that's frequently used:
              #print the 10 most common words and their counts:
              for word, count in word_counts.most_common(10):
                print(word, count)
              
  
#(8) Sets: represent a collection of distinct elements
              s = set()
              s.add(1)    #s is now {1}
              s.add(2)    #s is now {1, 2}
              s.add(2)    #s is still {1,2} 
              x = len(s)  #equals 2
              y = 2 in s  #returns True
              z = 3 in s  #returns False
     
        #sets are convenient for testing memberships
      
        #in is a very fast operator we can use with sets:
              stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
              
              "zip" in stopwords_list   # False, but have to check every element
              
              stopwords_set = set(stopwords_list)
              zip in stopwords_set                # very fast check: Basically we cast as a SET and use IN for membership.
              
        #sets are also good for finding DISTINCT items in a collection
  
#(9) Control Flow: performing actions conditionally
             # if
             # elif
             # else
              
             #ternary if-then-else on one line:    parity = "even" if x % 2 == 0 else "odd"
              
             #for/in:      
              for x in range(10)
                print(x, "is less than 10")
             
             #continue/break
              for x in range(10):
                if x == 3:
                  continue   # go immediately to the next iteration
                if x == 5: 
                  break      # quit the loop entirely
              print(x)
              #this will print 0, 1, 2, and 4
              
#(10) Sorting:
              x = [4, 1, 2, 3]
              y = sorted(x)     # is [1,2,3,4], is is unchanged
              x.sort()          # now x is [1,2,3,4]
              
              #you can also sort a list by absolute value from largest to smallest, by using KEY and REVERSE
              x = sorted([-4, 1, -2, 3], key=abs, reverse=True) # is [-4,3,-2,1]
              
              
#(11) List Comprehensions: transforms a list into another list by using only certain elements or by transforming elements, or both
              even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
              squares      = [x * x for x in range(5)]            #[0,1,4,9,16]
              even_squares = [x * x for x in even_numbers]        #[0, 4, 16]
              
           #you can also similarily turn lists into dictionaries or sets:
              square_dicts = { x : x * x for x in range(5) }  # { 0:0, 1:1, 2:4, 3:9, 4:16}
              square_set   = { x * x for x in [1, -1] }       # { 1 }

           #a list comprehension can include multiple for loops:
              pairs = [(x, y)
                       for x in range(10)
                       for y in range(10)            #100 pairs (0,0) (0,1)...(9,8), (9,9)
                       
#(12) Generators: a problem with lists is that they can easily grow very large. If you only need to the first few values, then calculating them all is a waste
        #a generator is something you can iterate over, but whose values are produced only as needed
        #example of a generating using a yield operator:
                       def lazy_range(n):
                            """a lazy version of range"""
                            i = 0 
                            while i < 0:
                                yield i
                                i += 1
                       
                       for i in lazy_range(10): 
                          do_something_with(i)
        #note that you can only iterate through a generator once. 
        #if you need to iterate thoguht something multiple times then you need to recreate the generator each time or use a list.
        
     #another way to create a generator is by using for comprehensions wrapped in parentheses:
      lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
                       
#(13) Randomness: 
        import random
        four_uniform_randoms = [random.random() for _ in range(4)]
                       #[0.84    #random.random() produces numbers
                       #0.75     #uniformly between 0 and 1
                       #0.42     #it's the most random function we'll use
                       #0.25     #most often
                       
        #random.randrange    
                       random.randrange(10)  #chooses randomly from range(10)   =  [0, 1, 2....9]
                       random.randrange(3, 6) #chooses randomly from range(3,6) =  [3, 4, 5]
        #random.shuffle
                       #randomly reorders the elements of a list
                       up_to_ten = range(10)
                       random.shuffle(up_to_ten)
                       print(up_to_ten)
        #random.sample
                       #randomly chooses a sample of elements with no duplicates
                 
        #random.choice
                       #same thing as random.sample, but allows for duplicates
                      
 #(14) Object Oriented Programming
       #allows you to define classes and the functions that operate within them
       def _init_(self, values = None):
       #this is the constructor. It gets called when you create a new set.
                       
  
#(15) Functional Tools
      #when passing functions around, sometimes we'll want to partially apply (or curry) functions to create new functions
      #functools.partial
                       from functools import partial
                       tow_to_the = partial(exp, 2)
                       print(two_to_the(3))
                       
#(16) Enumerate:
      #iterate over a list and use both its elements and their indexes 
      #enumerate produces tuples(index, element):
                       for i, document in enumerate(documents):         #pythonic
                          do_something(i, document)
                       
                       for i in range(len(documents)):                  #not pythonic
                          document = documents[i]
                          do_something(i, document)
                       
                       i = 0                                            #not pythonic
                       for document in documents:
                          do_something(i, document)
                          i += 1
                                      
                       
     #similarily, if we just want the indexes:
                       for i in range(len(documents)): do_something(i)         #not pythonic
                       
                       for i, _ in enumerate(documents): do_something(i)        #pythonic
                       
                       
#(17) Zip and Argument Unpacking: zip()
      #often we need to zip two or more lists together. ZIP() transforms multiple lists into a single list of tuples of corresponding elements
      list1 = ['1', 'b', 'c']
      list2 = [1, 2, 3]
      zip(list1, list2)   #is [('a', 1), ('b', 2), ('c', 3)]
                       #if lists are different sizes, zip() stops as soon as the first list ends.
                       
      #unzipping: use x, y = zip(*pairs):
                       pairs = [('a', 1), ('b', 2), ('c', 3)]
                       letters, numbers = zip(*pairs)
                       
                 #the * performs the argument unpacking, returns:
                       #[('a', 'b', 'c'), ('1', '2', '3')]
                       
 #(18) Args and Kwargs
                       
       
                       
             
