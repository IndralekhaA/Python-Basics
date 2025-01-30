#Sets-Mutable,unordered & Unique-{,,,}
set_1 = {1,2,3}
print(type(set_1))

set_2 = set()
print(type(set_2))

#add()
set_1 = {1,2,3}
set_1.add(5)
print(set_1)

#update()
my_set = {1,2, (1,2)}
set_2 = {3,4, (5,6)}
my_set.update(set_2)
print(my_set)

#remove()--raises error if ele not exists in set 
my_set = {1,2, (1,2)}
my_set.remove(1)
print(my_set)
#discard()--doesn't raise error 
my_set = {1,2, (1,2)}
my_set.discard(3)
print(my_set)

#pop() removes and returns a random element
my_set = {101,2, (1,2), "hello", 3,5.5, 1000}
obj = my_set.pop()
print(obj)
#clear()
my_set = {101,2, (1,2), "hello", 3,5.5, 1000}
my_set.clear()
print(my_set)
#copy()
my_set = {101,2, (1,2), "hello", 3,5.5, 1000}
obj = my_set.copy()
print(obj)
#len()
my_set = {101,2, (1,2), "hello", 3,5.5, 1000}
print(len(my_set))

#########   Operators   ########
union()
set_1 = {1,2,3,4,5}
set_2 = {1,2,3}
union_set = set_1.union(set_2)
print(union_set)
print(set_2)
print(set_1)

set_1 = {1,2,3,4,5}
set_2 = {1,2,3}
union_set = set_1|set_2
print(union_set)
print(set_1)
print(set_2)


#intersection()
set_1 = {1,2,3,4,5}
set_2 = {1,2,3}
intersection_set = set_2.intersection(set_1)
print(set_1)
print(set_2)
print(intersection_set)

set_1 = {1,2,3,4,5}
set_2 = {1,2,3}
intersection_set = set_2 & set_1
print(set_1)
print(set_2)
print(intersection_set)

#difference()
set_1 = {1,2,3,4,5}
set_2 = {1,2,3,6}
difference_set = set_2.difference(set_1)
print(set_1)
print(set_2)
print(difference_set)

set_1 = {1,2,3,4,5}
set_2 = {1,2,3,6}
difference_set = set_2 - set_1
print(set_1)
print(set_2)
print(difference_set)#6

#symmetric-difference
set_1 = {1,2,3,4,5}
set_2 = {1,2,3,6}
sym_set = set_1.symmetric_difference(set_2)
print(set_1)
print(set_2)
print(sym_set)

set_1 = {1,2,3,4,5}
set_2 = {1,2,3,6}
sym_set = set_1 ^ set_2
print(set_1)
print(set_2)
print(sym_set)#{4,5,6}

#isdisjoint()--
set_1 = {1,2,4}
set_2 = {2}
print(set_1.isdisjoint(set_2))

#superset()
set_1 = {1,2,3,4,5}
set_2 = {2,3,4}
print(set_1.issubset(set_2))#False
print(set_1.issuperset(set_2))#True
print(set_1 <= set_2)#subset--False
print(set_1 >= set_2)#superset- True

#FROZENSET()
my_set = {1,"Indra", 3.6, (1,2)}
print(frozenset(my_set))
print({1,"Indra", 3.6, (1,2)})

set_1 = frozenset({1,2,3,4,6})
set_2 = frozenset({2,3,5})

print(set_1.difference(set_2))
print(set_1.intersection(set_2))
print(set_1.union(set_2))
print(set_1.issubset(set_2))
print(set_1.issuperset(set_2))
print(set_1.isdisjoint(set_2))
print(set_1.symmetric_difference(set_2))





#### SET COMPREHENSIONS ####
my_set = {x ** 2 for x in range(5)} # {0, 1, 4, 9, 16}
print(my_set)


my_set = {x+(x*18/100) for x in range(10)} # 18% added to the number
print(my_set)















