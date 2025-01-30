##########  TUPLES  ##########
#definition-(,,,)--IMMUTABLE,ORDERED
my_tuple = (1,2,3,5)
tuple_2 = ()
tuple_3 = tuple()
print(type(my_tuple))
print(type(tuple_2))
print(type(tuple_3))

#len()
tuple_1 = (1,"New York", 98.5, 1010)
print(len(tuple_1))

#count()
tuple_1 = (1,"New York", 98.5, 1010,2, 4,2,2,2,2,2)
print(tuple_1.count(2))

#index()
tuple_1 = (1,"New York", 98.5, 1010,2, 4,2,2,2,2,2)
print(tuple_1.index(2))#4 , first occurence of 2 is at index 4


#Slicing
my_tuple = (1,2,3,4,5,1,2,3,4,1,2,3,5,2,4,7,6)
print(my_tuple[-1])#6
print(my_tuple[1])#2
print(my_tuple[1:5])#2,3,4,5 in tuple
print(my_tuple[-6:-2])#3,5,2,4 in tuple
print(my_tuple[-2:-6:-1])#7,4,2,5 in tuple
print(my_tuple[8:3:-1])#4,3,2,1,5 in tuple

tuple_1 = tuple("Hello")
print(tuple_1)




#####   Tuple Operations ######
#Concatenation
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
result_tuple = tuple1 + tuple2
print(result_tuple)

# Repetition
tuple1 = (1, 2, 3)
result_tuple = tuple1*2
print(result_tuple)

#Membership Test
fruits = ("Orange" ,"Apple", "Banana", "Cherry", "Parsimon")
is_apple_present = "Apple" in fruits
print(is_apple_present)

#all()
my_tuple = (1,2,3,4,5,1,2,3,4,1,2,3,5,2,4,7,6)
print(all(my_tuple))
tuple_1 = ()
print(all(tuple_1))




