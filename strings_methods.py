#Strings-Seqn of characters- textual info. stored-defined by '',"",""" """.
single_quote = ' Hello '
double_quote = " Helloo"
triple_quote = """ Hellooo
How are you?
"""
print(type(single_quote))
print(type(double_quote))
print(type(triple_quote))



s = "hello How Are you?"
print(s.capitalize())

'''
str.casefold()
Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.

Casefolding is similar to lowercasing but more aggressive because it is intended to remove
all case distinctions in a string.
For example, the German lowercase letter 'ß' is equivalent to "ss".
Since it is already lowercase, lower() would do nothing to 'ß'; casefold() converts it to "ss".

'''
#str.center(width[, fillchar])

#str.count(sub[, start[, end]])
s = "Return the number of non-overlapping occurrences of substring sub in the range [start, end]"
print(s.count("the"))# the substring "the" occurs twice
print(s.count("r"))# the substring "r" occurs 8 times omits the 'R'


#str.expandtabs(tabsize=8)
s = "That\tis\ttoo\t far"
print(s.expandtabs(tabsize=2))
print(s.expandtabs(tabsize=4))
print(s.expandtabs(tabsize=8))
print(s.expandtabs(tabsize=10))

#str.isalnum()
s = "T1A"
print(s.isalnum())

#str.isdecimal()

#str.isdigit()
s = "1123"
print(s.isdigit())

#str.join(iterable)
s1 = ["Hello", "Hi", "How", "Are", "You?"]
obj = " ,".join(s1)#returns string
print(obj)
print(type(obj))

#str.strip([chars])-- .rstrip() & .lstrip()
s = "     I am not good at this. I hope     everything goes well!   "
print(s.strip()) #removes white spaces at the both ends, not within!

#str.replace(old, new, count=-1)--- Changed in version 3.13: count is now supported as a keyword argument.
s = "This is very godly very very good!"
print(s.replace("very", "too"))
print(s.replace("very", "too", -1))# Default-replces all occurences of substring
print(s.replace("very", "too", 1)) #replaces first occurence
print(s.replace("very", "too", 2))#replaces first 2 occurences
print(s.replace("very", "too", 3))#replaces first 3 occurences


#str.swapcase()
s = "Return a copy of the string with uppercase characters converted to lowercase and vice versa.!"
print(s.swapcase())

#str.title()
s = "Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase."
print(s.title())

#str.find(sub[, start[, end]])----  .
s = "Can you find the specified substring in the given string"
print(s.find("string",0,36))#start index 0-end index 36-returns index no. of 1st occurence
print(s.find("ing"))#by default start to end
print(s.find("India"))#returns -1 unlike index()-returns error

#str.rfind()----returns highest index.
s = "Hello Hi How are you?"
print(s.rfind("H"))#9 , H indices are 0,6,9

#str.index(sub[, start[, end]])
s = "Can you find the specified substring in the given string"
print(s.index("in",11,16))#"in" is at index 9, but start-end is 11-16, there is no in, gives error
print(s.index("India"))# given substring not found, gives error unlike find() which returns -1

#str.rindex(sub[, start[, end]]) - 
s = "Hello Hi, are you there?"
print(s.rindex("e"))#22, e indices are 1,12,20,22

#str.islower() & str.isupper() 
s = "this is lower case"
print(s.islower())
print(s.isupper())

#Index- +ve & -ve
s = "RrRrRrRrRrRr"
print(s[::-1])
print(s[0::3])



#LEETCODE PROBLEM - Words merging alternately need to find solution
#zip_longest()----itertools — Functions creating iterators for efficient looping
word1 = "abc"
word2 = "pqr"
merged_word = str()
for i in word1:
    for j in word2:
       
print(merged_word)

#finding vowels in given string
s = "Return a copy of the string with leading characters removed."
vowels = "aeiouAEIOU"
print([f" {i} comes {s.count(i)} times" for i in vowels if i in s])
new_string = str([i for i in vowels if i in s])
print(f"Out of {len(s)}, There are {len(new_string)} vowels and {len(s)-len(new_string)} consonents in the given string")





