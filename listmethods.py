#List and it's methods
my_list = [1, 2, 5.5,"winter", True]
print(type(my_list))

list_1 = []
print(type(list_1))

list_2 = list()
print(type(list_2))

# List - indexing
# Positive indexing
list_1 = [1, 5.5, "apple", "rose", 22, 1.5, [2,3.4,"Yes"], (22,33,44), {9,1.40,(2,True,"Hi")}, False]
print(list_1[0]) #1
print(list_1[2]) #apple
print(list_1[4]) #22
print(list_1[6]) #[2,3.4,"Yes"]
print(list_1[8]) #{9,1.40,(2,True,"Hi")} - Unordered


# Negative indexing
list_1 = [1, 5.5, "apple", "rose", 22, 1.5, [2,3.4,"Yes"], (22,33,44), {9,1.40,(2,True,"Hi")}, False]
print(list_1[-1]) #False
print(list_1[-4]) #[2,3.4,"Yes"]
print(list_1[-9])#5.5
print(list_1[-6])#22

Modification- Mutable

list_1 = [1, 5.5, "apple", "rose", 22, 1.5, [2,3.4,"Yes"], (22,33,44), {9,1.40,(2,True,"Hi")}, False]
list_1[2] = "rabbit"
print(list_1)

Slicing
my_list = [1, 5.5, "apple", "rose", 22, 1.5, [2,-3.4,"Yes"], (22,33,44), [9,1.40,(2,True,"Hi")], False]
print(my_list[::]) #start:stop:step
print(my_list[::1]) #start:stop:step
print(my_list[::2]) #start:stop:step
print(my_list[2:6]) #start:stop(n-1 retrives)
print(my_list[5:-1])
print(my_list[-5:])
print(my_list[-5::1])
print(my_list[-1:-5:-1]) 
print(my_list[-5:-1:1]) 

#task to print different types of numbers from the list using slicing
list_of_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] 
print(list_of_numbers[::])#all numbers
print(list_of_numbers[0::2])#odd numbers
print(list_of_numbers[1::2])#even numbers
print(list_of_numbers[::-1])#all numbers backward
print(list_of_numbers[-2::-2])#even numbers reverse order
print(list_of_numbers[-1::-2])#odd numbers reverse order
print(list_of_numbers[:10:2])#odd numbers till 10
print(list_of_numbers[1:10:2])#even numbers till 10
print(list_of_numbers[-2:-7:-2])#even numbers till 10 in reverse order, -ve indexing
print(list_of_numbers[-1:-7:-2])#odd numbers till 10 in reverse order, -ve indexing
print(list_of_numbers[13:8:-2])#odd numbers till 10 in backward but +ve indexing
print(list_of_numbers[14:8:-2])#even numbers till 10 in backward but +ve indexing

#LIST-METHODS

list_1 = [1, 5.5, "apple", "rose", 22, 1.5, [2,3.4,"Yes"], (22,33,44), False]
list_1.append(["NextOne", "SecondNext"])
print(list_1)

list_1 = [1,3,5,7,9]
list_2 = [2,4,6,8,10]
list_1.extend(list_2)
print(list_1)
print(list_2)
copy_list = list_1.copy()
print(copy_list)
copy_list.clear()
print(copy_list)

numbers = [2,4,6.6,88,10,4,2,4,2,2,2]
print(numbers.count(44))
numbers = [2,4,6.6,88,10,4,2,4,2,2,2]
print(numbers.index(10))
print(numbers.index(2))
numbers = [2,4,6.6,88,10,4,2,4,2,2,2]
numbers.remove(4)
print(numbers)

numbers = [2,4,6.6,88,10,4,2,4,2,2,2]
numbers.pop(-1)
popped_num = numbers.pop(2)
print(numbers)
print(popped_num)

numbers = [2,4,6.6,88,10,4,2,4,2,2,2]
numbers.insert(0,5)
print(numbers)

numbers = [2,4,6.6,88,10,4,2,4,2,2,2]
numbers.reverse() # can also be done with slicing
print(numbers) 

numbers = [2,4,6.6,88,10,4,2,4,2,2,2]
numbers.sort()
numbers.sort(reverse=True)
print(numbers)

numbers = [2,4.5, -1, 3.4, 2.1, -6]
numbers.sort(reverse=True)
print(numbers)

#Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][0])
print(matrix[1][0])
print(matrix[2][1])


#list comprehensions
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(f"common elements in both the lists are :{[i for i in list1 for j in list2 if i==j]}")

















