
# Advanced Data Structures

# lists, tuples, sets, and dictionaries

# Lists: Description: Ordered and mutable collection of items.
# Example: 
[1, 2, 3, 4, 5]

# Lists are mutable ordered sequences of elements
# Example: 
[1, 2, 3, 4, 5]

# Lists are defined by square brackets
# Example: 
[1, 2, 3, 4, 5]

# Lists can contain any data type
# Example: 
[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

# Lists can be nested
# Example: 
[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e', [1, 2, 3, 4, 5]]

# Lists can be accessed by index
# Example: 
list = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e', [1, 2, 3, 4, 5]]
print(list[0]) # 1
print(list[1]) # 2
print(list[2]) # 3
print(list[3]) # 4
print(list[4]) # 5
print(list[5]) # a
print(list[6]) # b
print(list[7]) # c

# Lists can be sliced
# Example: 
list = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e', [1, 2, 3, 4, 5]]
print(list[0:2]) # [1, 2]
print(list[1:3]) # [2, 3]
print(list[2:4]) # [3, 4]
print(list[3:5]) # [4, 5]
print(list[4:6]) # [5, 'a']
print(list[5:7]) # ['a', 'b']
print(list[6:8]) # ['b', 'c']
print(list[7:9]) # ['c', 'd']

# Lists can be modified
# Example: 
list = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e', [1, 2, 3, 4, 5]]
list[0] = 10
list[1] = 20
list[2] = 30
print(list) 
# output =  [10, 20, 30, 4, 5, 'a', 'b', 'c', 'd', 'e', [1, 2, 3, 4, 5]]

# Lists can be sorted
# Example:  
list = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e', [1, 2, 3, 4, 5]]
list.sort()
print(list)
# output = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 'a', 'b', 'c', 'd', 'e']

# Lists can be reversed
# Example: 
list = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e', [1, 2, 3, 4, 5]]
list.reverse()
print(list)
# output = [[1, 2, 3, 4, 5], 'e', 'd', 'c', 'b', 'a', 5, 4, 3, 2, 1]

# Lists can be concatenated
# Example:
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = list1 + list2
print(list3)
# output = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
# Example:
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = list2 + list1
print(list3)
# output = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5]

# Lists can be copied
# Example:
list1 = [1, 2, 3, 4, 5]
list2 = list1.copy()
print(list2)
# output = [1, 2, 3, 4, 5]

# Lists can be extended
# Example:  
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list1.extend(list2)
print(list1)
# output = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

# Lists can be cleared
# Example:
list1 = [1, 2, 3, 4, 5]
list1.clear()
print(list1)
# output = []

# Lists can be deleted
# Example:
list1 = [1, 2, 3, 4, 5]
del list1
print(list1)
# output = NameError: name 'list1' is not defined

# Lists can be iterated over
# Example:
list = [1, 2, 3, 4, 5]
for item in list:
    print(item)
# output = 1
#          2
#          3
#          4

# Lists can be iterated over with index
# Example:
list = [1, 2, 3, 4, 5]
for index, item in enumerate(list):
    print(index, item)
# output = 0 1
#          1 2
#          2 3
#          3 4
#          4 5

# Lists can be iterated over with index and start
# Example:
list = [1, 2, 3, 4, 5]
for index, item in enumerate(list, start=1):
    print(index, item)
# output = 1 1
#          2 2
#          3 3
#          4 4
#          5 5
    
# Lists can be converted to tuples
# Example:
list = [1, 2, 3, 4, 5]
tuple = tuple(list)
print(tuple)
# output = (1, 2, 3, 4, 5)

# Lists can be converted to sets
# Example:
list = [1, 2, 3, 4, 5]
set = set(list)
print(set)
# output = {1, 2, 3, 4, 5}

# Lists can be converted to dictionaries
# Example:
list = [1, 2, 3, 4, 5]
dict = dict.fromkeys(list)
print(dict)
# output = {1: None, 2: None, 3: None, 4: None, 5: None}

# Lists can be converted to strings
# Example:
list = [1, 2, 3, 4, 5]
string = str(list)
print(string)
# output = [1, 2, 3, 4, 5]

# Lists can be converted to bytes
# Example:
list = [1, 2, 3, 4, 5]
bytes = bytes(list)
print(bytes)
# output = b'\x01\x02\x03\x04\x05'

# Lists can be converted to byte arrays
# Example:
list = [1, 2, 3, 4, 5]
bytearray = bytearray(list)
print(bytearray)
# output = bytearray(b'\x01\x02\x03\x04\x05')

# Lists can be converted to memory views
# Example:
list = [1, 2, 3, 4, 5]
memoryview = memoryview(list)
print(memoryview)
# output = <memory at 0x0000024E9D1D4C48>

# Lists can be converted to generators
# Example:
list = [1, 2, 3, 4, 5]
generator = (x for x in list)
print(generator)
# output = <generator object <genexpr> at 0x0000024E9D1D4C48>

# Lists can be converted to iterators
# Example:
list = [1, 2, 3, 4, 5]
iterator = iter(list)
print(iterator)
# output = <list_iterator object at 0x0000024E9D1D4C48>

# Lists can be converted to functions
# Example:
list = [1, 2, 3, 4, 5]
function = lambda x: x in list
print(function)
# output = <function <lambda> at 0x0000024E9D1D4C48>

# Lists can be converted to classes - creation of a class instance that contains a list as one of its attributes.
# Example:
list = [1, 2, 3, 4, 5]
class Class:
    def __init__(self, list):
        self.list = list
    def __str__(self):
        return str(self.list)
class_instance = Class(list)
print(class_instance)
# output = <__main__.Class object at 0x0000024E9D1D4C48>

# Lists can be converted to instances
# Example:
list = [1, 2, 3, 4, 5]
class Class:
    def __init__(self, list):
        self.list = list
    def __str__(self):
        return str(self.list)
class_instance = Class(list)
print(class_instance)
# output = <__main__.Class object at 0x0000024E9D1D4C48>

# Lists can be converted to booleans

# Lists can be converted to integers

# Lists can be converted to floats

# Lists can be converted to complex numbers

# Lists can be converted to hexadecimals

# Lists can be converted to octals

# Lists can be converted to binaries

# Lists can be converted to ascii characters

# Lists can be converted to unicode characters

# Lists can be converted to objects

# Lists can be converted to strings

# Key list operations: append, extend, insert, remove, pop, index, count, sort, reverse.

# append: Adds an element at the end of the list

# extend: Add the elements of a list (or any iterable), to the end of the current list

# insert: Adds an element at the specified position

# remove: Removes the item with the specified value

# pop: Removes the element at the specified position

# clear: Removes all the elements from the list

# index: Returns the index of the first element with the specified value

# count: Returns the number of elements with the specified value

# sort: Sorts the list

# reverse: Reverses the order of the list

# copy: Returns a copy of the list

# del: Deletes the list

# List comprehension: A concise way to create lists.

# List comprehension is an elegant way to define and create lists based on existing lists.

# List comprehension is generally more compact and faster than normal functions and loops for creating list.

# Good to remember: However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.

# Every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.

