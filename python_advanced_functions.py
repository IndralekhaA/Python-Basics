#### ***** ADVANCED FUNCTIONS ***** #####
#Lambda Function
#SYNTAX
#lambda parameters: expression
add = lambda num1, num2 :num1+num2
print(add(1,2))

multy = lambda num_1, num_2:num_1*num_2 
print(multy(4,7))

sub = lambda a,b: a - b
print(sub(6,7))

extended_len = lambda a,b: len(a)*b
print(extended_len("PythonLife",10))


### Filter function ###
#SYNTAX
#filter(function, iterable)
def is_odd(i):
    return i%2!=0
nums = [1,2,3,4,5,6,9]
obj = filter(is_odd,nums)
print(list(obj))

obj = filter(lambda i:i%2 ==0,[2,3,45,6,7,88,912,33])
print(list(obj))

obj = filter(lambda i:i%2 !=0,[2,3,45,6,7,88,912,33])
print(list(obj))


#itertools — Functions creating iterators for efficient looping
import itertools
#itertools.filterfalse(predicate, iterable)--returns ele, when function is false
obj = itertools.filterfalse(lambda i:i%2 ==0,[2,3,45,6,7,88,912,33])#---Need to know
print(list(obj))
#itertools.dropwhile(predicate, iterable)--Make an iterator that drops elements from the iterable while the predicate is true and afterwards returns every element
obj_2 = itertools.dropwhile(lambda x: x<45,[2,32,43,12,41,18,46,1,54,21])#46,1,54,21
print(list(obj_2))


##### map function  ####
#SYNTAX
#map(function, iterable, *iterables)

obj = map(lambda x,y: x+y ,[1,2,3,4,5,9,12,32,11,35],(4,2,5,6,2,6,1,34))
print(list(obj))

first_names = ["Ram", "Raj", "Sai"]
last_names = ["Reddy","K", "M"]

obj = map(lambda first, last:f" {first} {last}",first_names, last_names )
print(list(obj))

###### reduce function ######
from  functools import reduce
obj = reduce(lambda x,y: x+ y , [1,2,3,4,5])
print(obj)

#### Generator function ####
#yield keyword
def fun_1():
    yield 1 #pause or hold
    yield 2
    yield 3

obj = fun_1()
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())




