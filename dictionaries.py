#Dictionary-defined {key1:value1, key2:value2...}
#Keys(CASE SENSITIVE)-Unique,immutable(NTS), Values-Any Type

my_dict = {}
print(type(my_dict))

my_dict = {
"a":1, 
"b":2, 
"c":3
}
print(type(my_dict))

sample_2 = dict()
print(type(sample_2))

#clear()---Remove all items from the dictionary.
sample_1 = {
    "a":1, 
    "b":2, 
    "c":3
}
sample_1.clear()
print(sample_1)

#copy()---Return a shallow copy of the dictionary.
sample_1 = {
    "a":1, 
    "b":2, 
    "c":3
}
copy_sample = sample_1.copy()
print(copy_sample)

#get(key, default=None)---
"""Return the value for key if key is in the dictionary, else default.
If default is not given, it defaults to None, so that this method never raises a KeyError
"""
sample_1 = {
    "a":1, 
    "b":2, 
    "c":3
}
print(sample_1.get("d"))#returns None, doesn't raises error.
print(sample_1.get("a"))#returns value of given key

sample_1 = {
    "a":1, 
    "b":2, 
    "c":3
}
print(sample_1["b"])#returns the value of key given.
print(sample_1["d"])#Raises error if the given key value not present in dict.

#items()---Return a new view of the dictionary’s items ((key, value) pairs).
sample_1 = {
    "a":1, 
    2 :2025, 
    "c":3
}
print(sample_1.items())#returns value (key,value) pairs in tuple

#keys()---Return a new view of the dictionary’s keys.
sample_1 = {
    "a":1, 
    2 :2025, 
    (4,9):[4,8]
}
print(sample_1.keys())

#pop(key[, default])---If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised
sample_1 = {
    "a":1, 
    2 :2025, 
    (4,9):[4,8]
}
print(sample_1.pop("a"))#1
print(sample_1)
print(sample_1.popitem())#removes and returns last (key,value)pair as tuple
print(sample_1.popitem())#removes and returns last (key,value)pair as tuple
print(sample_1)


#update([other])---Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.
sample_1 = {
    "branch": 1, 
    "location" :"NYC",
    "total_dept" : 7,
}
sample_2 = {
    "Dept_id" : 1001,
    "Dept_name" : "Science"
}
sample_1.update(sample_2)#sample_1 updates with sample_2 data
print(sample_1)
print(sample_2)

my_dict = {
"a":1, 
"b":2, 
"c":3
}
print(my_dict)
my_dict["d"] = 1212#Add New Key-Value pair
my_dict["c"] = 3030#replaces value for key "c"
print(my_dict)

'''
#add()
my_dict = {
"a":1, 
"b":2, 
"c":3
}
print(my_dict)
sample_1 = {
    "d" : 1234
}
my_dict.add(sample_1)#AttributeError: 'dict' object has no attribute 'add'
print(my_dict)

#insert()
my_dict = {
"a":1, 
"b":2, 
"c":3
}
print(my_dict)
sample_1 = {
    "d" : 1234
}
my_dict.insert("e",123)#AttributeError: 'dict' object has no attribute 'insert'
print(my_dict)


#append()
my_dict = {
"a":1, 
"b":2, 
"c":3
}
print(my_dict)
sample_1 = {
    "d" : 1234
}
my_dict.append(sample_1)#AttributeError: 'dict' object has no attribute 'append'
print(my_dict)
'''


#values()---Return a new view of the dictionary’s values.
sample_1 = {
    "branch": 1, 
    "location" :"NYC",
    "total_dept" : 7,
}
print(sample_1.values())#dict_values([1, 'NYC', 7])

#reversed(d)---Return a reverse iterator over the keys of the dictionary.
sample_1 = {
    "branch": 1, 
    "location" :"NYC",
    "total_dept" : 7,
}
for i in reversed(sample_1):
    print(i)

#del(d[key])---remove the specified key of the dict, Error if no key exists in dict
sample_1 = {
    "branch": 1, 
    "location" :"NYC",
    "total_dept" : 7,
}
del(sample_1["total_dept"])
print(sample_1)
print("total_dept" in sample_1)

























