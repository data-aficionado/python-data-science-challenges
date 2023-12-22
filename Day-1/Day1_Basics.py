# Indentation: Python uses indentation to define blocks of code. This is different from languages like Java or C++, which use curly braces. Indentation must be consistent in your code. Otherwise, you will get an IndentationError.
if 5 > 2:
    print("Five is greater than two!")
# Comments: Python uses the hash (#) symbol to start writing a comment.
# This is a comment
print("Hello, World!")
#Variables: Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.
x = 5
y = "Hello, World!"

# Basic Data Types: Python has several built-in data types. The most common ones are:
    # Integers: Whole numbers without a fractional part.
x = 5

    # Floats: Any real number with a floating point representation in which a fractional component is denoted by a decimal symbol or scientific notation 1.43 or 2.67e2.
y = 5.0

    # Strings: A sequence of one or more characters enclosed within either single quotes (') or double quotes (").
greeting = "Hello"
name = 'World'

    # Booleans: A binary variable having two possible values called "true" and "false".
my_boolean = True
print(my_boolean)

is_valid = True
print(is_valid)

is_invalid = False
print(is_invalid)

# Operators: Operators are used to perform operations on variables and values.
    # Arithmetic Operators: Arithmetic operators are used with numeric values to perform common mathematical operations.
x = 5
y = 3

print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulus
print(x ** y) # Exponentiation
print(x // y) # Floor division

    # Assignment Operators: Assignment operators are used to assign values to variables.
x = 5

print(x)

x += 3 # x = x + 3
print(x)

x -= 3 # x = x - 3
print(x)

x *= 3 # x = x * 3
print(x)

x /= 3 # x = x / 3
print(x)

x %= 3 # x = x % 3
print(x)

x //= 3 # x = x // 3
print(x)

x **= 3 # x = x ** 3
print(x)
    
    # Comparison Operators: Comparison operators are used to compare two values.
x = 5
y = 3

print(x == y) # Equal
print(x != y) # Not equal
print(x > y) # Greater than
print(x < y) # Less than
print(x >= y) # Greater than or equal to
print(x <= y) # Less than or equal to

    # Logical Operators: Logical operators are used to combine conditional statements.
x = 5

print(x > 3 and x < 10) # and: Returns True if both statements are true
print(x > 3 or x < 4) # or: Returns True if one of the statements is true

print(not(x > 3 and x < 10)) # not: Reverse the result, returns False if the result is true
    
     # Identity Operators: Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # is: Returns True if both variables are the same object
print(x is y)
print(x == y) # ==: Returns True if both variables are the same object

print(x is not z) # is not: Returns True if both variables are not the same object
print(x is not y)


    # Membership Operators: Membership operators are used to test if a sequence is presented in an object
x = ["apple", "banana"]
print("banana" in x) # in: Returns True if a sequence with the specified value is present in the object   

print("pineapple" not in x) # not in: Returns True if a sequence with the specified value is not present in the object
    
        # Bitwise Operators: Bitwise operators are used to compare (binary) numbers
x = 5 # 0101
y = 3 # 0011

print(x & y) # & AND: Sets each bit to 1 if both bits are 1
print(x | y) # | OR: Sets each bit to 1 if one of two bits is 1
print(x ^ y) # ^ XOR: Sets each bit to 1 if only one of two bits is 1
print(~x) # ~ NOT: Inverts all the bits
print(x << y) # << Zero fill left shift: Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(x >> y) # >> Signed right shift: Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# Control Structures: Control structures in Python are used to direct the flow of code execution based on conditions and loops.

# If-Else Statement:

# Used to execute code based on a condition.
# elif and else are optional.
# elif is short for else if.
# else is a catch all condition.
# if condition1:
#     statement1
# elif condition2:
#     statement2
# else:
#     statement3

# Example:
x = 5
y = 3

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x and y are equal")

 #Example:
age = 20
if age >= 18:
    print("Adult")
elif age < 18 and age > 0:
    print("Child")
else:
    print("Invalid age")

# Loops:

# For Loop: Used for iterating over a sequence (like a list, tuple, dictionary, set, or string).   
# for item in sequence:
#     statement
    
# Example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

 #Example:
for x in "banana":
    print(x)

  #Example:
for x in range(6):
    print(x)

# Example:
    fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# While Loop: Used to execute a set of statements as long as a condition is true.
# while condition:
#     statement
    
 # Example:
    count = 0
while count < 5:
    print(count)
    count += 1


# Example:
i = 1
while i < 6:
    print(i)
    i += 1

# Example:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Example:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#-------------------------------------------Examples----------------------------
#-------------------------------------------------------------------------------
# Example 1: Write a program to find the sum of all elements of a list.
# Solution 1: Using for loop
# list of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

# Output: The sum is 48
print("The sum is", sum)

# Solution 2: Using while loop
# list of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0
i = 0

# iterate over the list
while(i < len(numbers)):
    sum = sum + numbers[i]
    i = i+1

# Output: The sum is 48
print("The sum is", sum)

# Example 2: Write a program to find the largest number in a list.
# Solution 1: Using for loop
# list of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the largest number
largest_number = numbers[0]

# iterate over the list
for val in numbers:
    # compare elements of the list with largest_number and
    # if the element is greater, then update largest_number
    if val > largest_number:
        largest_number = val


# Output: The largest number is 11
print("The largest number is", largest_number)

# Solution 2: Using while loop
# list of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the largest number
largest_number = numbers[0]
i = 1

# iterate over the list
while(i < len(numbers)):
    # compare elements of the list with largest_number and
    # if the element is greater, then update largest_number
    if(numbers[i] > largest_number):
        largest_number = numbers[i]
    i = i+1

# Output: The largest number is 11
print("The largest number is", largest_number)

# Example 3: Write a program to find all prime numbers between two intervals.
# Solution 1: Using for loop
# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num)

# Solution 2: Using while loop
# Python program to display all the prime numbers within an interval
            
lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

while(lower < upper):
    isPrime = True;
    if(lower == 0 or lower == 1):
        isPrime = False
    else:
        for i in range(2, lower):
            if(lower % i == 0):
                isPrime = False
                break
    if(isPrime):
        print(lower)
    lower = lower + 1

# Example 4: Write a program to check if a number is prime or not.
# Solution 1: Using for loop
# Python program to check if the input number is prime or not
    
num = 407

# prime numbers are greater than 1

if num > 1:

    # check for factors
    for i in range(2, num):
        if(num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")


# Solution 2: Using while loop
# Python program to check if the input number is prime or not

num = 407

# prime numbers are greater than 1

if num > 1:

        # check for factors
        i = 2
        while(i < num):
            if(num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
            i = i + 1
        else:
            print(num, "is a prime number")



# Combining Data Types and Control Structures:

# Example 1: Write a program to check if a number if odd or even.
            numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
# Nested If-Else:

# Example 1: Write a program to check if a number is positive, negative or zero.
# Solution 1: Using for loop
# Python program to check if the input number is positive, negative or zero
        
numbers = [1, 2, 3, 0, -4, -5, 6, -7]
for num in numbers:
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")

# Solution 2: Using while loop
# Python program to check if the input number is positive, negative or zero
        
numbers = [1, 2, 3, 0, -4, -5, 6, -7]
i = 0

while(i < len(numbers)):
    if numbers[i] > 0:
        print(f"{numbers[i]} is positive")
    elif numbers[i] < 0:
        print(f"{numbers[i]} is negative")
    else:
        print(f"{numbers[i]} is zero")
    i = i+1

    # Example 3 
    num = 15
if num > 10:
    if num % 2 == 0:
        print("Number is greater than 10 and even")
    else:
        print("Number is greater than 10 and odd")
else:
    print("Number is 10 or less")

# String Operations:

# Example 1: Write a program to find the length of a string.
# Solution 1: Using for loop
# Python program to find the length of a string
    
str = "Hello World"
count = 0

for char in str:
    count = count+1

print("Length of the input string is:", count)

# Solution 2: Using while loop
# Python program to find the length of a string

str = "Hello World"
count = 0
i = 0

while(i < len(str)):
    count = count+1
    i = i+1


print("Length of the input string is:", count)

#Example 2: 
name = "Alice"
# Accessing characters
print(name[0])  # 'A'
# Length of the string
print(len(name))  # 5
# Concatenation
greeting = "Hello, " + name
print(greeting)  # "Hello, Alice"

# Daily Challenge: Write a program to check if a string is a palindrome or not.
# Solution 1: Using for loop
# Python program to check if the input string is a palindrome or not

my_str = "aIbohPhoBiA"

# make it suitable for caseless comparison

my_str = my_str.casefold()

# reverse the string

rev_str = reversed(my_str)

# check if the string is equal to its reverse

if list(my_str) == list(rev_str):
    print("It is palindrome")
else:
    print("It is not palindrome")

# Solution 2: Using while loop
# Python program to check if the input string is a palindrome or not
    
my_str = "aIbohPhoBiA"
my_str = my_str.casefold()
i = 0
j = len(my_str)-1
flag = True

while(i < j):
    if(my_str[i] != my_str[j]):
        flag = False
        break
    i = i+1
    j = j-1

if(flag):
    print("It is palindrome")
else:
    print("It is not palindrome")

# FizzBuzz Challenge:

#Write a program that prints the numbers from 1 to 100.
#For multiples of three print “Fizz” instead of the number, and for the multiples of five print “Buzz”.
#For numbers which are multiples of both three and five print “FizzBuzz”.
    
# Solution 1: Using for loop
# Python program to print Fizz Buzz
    
for fizzbuzz in range(100):
    # print numbers from 1 to 100
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

# Solution 2: Using while loop
# Python program to print Fizz Buzz
    
fizzbuzz = 0
while fizzbuzz < 100:
    # print numbers from 1 to 100
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
    elif fizzbuzz % 3 == 0:
        print("fizz")
    elif fizzbuzz % 5 == 0:
        print("buzz")
    else:
        print(fizzbuzz)
    fizzbuzz = fizzbuzz+1

# Solution 3: Using for loop and range function
# Python program to print Fizz Buzz
    
for fizzbuzz in range(100):
    # print numbers from 1 to 100
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
    elif fizzbuzz % 3 == 0:
        print("fizz")
    elif fizzbuzz % 5 == 0:
        print("buzz")
    else:
        print(fizzbuzz)

#Daily Challenge: Sum of Even Numbers:

# Given a list of numbers, write a Python program to find the sum of all even numbers in the list.
# Example 1: Using for loop
# Python program to find the sum of all even numbers in a given list
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_even = 0

for num in numbers:
    if num % 2 == 0:
        sum_even = sum_even+num

print("Sum of even numbers in the list:", sum_even)

# Example 2: Using while loop
# Python program to find the sum of all even numbers in a given list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_even = 0
i = 0

while(i < len(numbers)):
    if numbers[i] % 2 == 0:
        sum_even = sum_even+numbers[i]
    i = i+1

print("Sum of even numbers in the list:", sum_even)

# Daily Challenge: Sum of Odd Numbers:

# Given a list of numbers, write a Python program to find the sum of all odd numbers in the list.
# Example 1: Using for loop
# Python program to find the sum of all odd numbers in a given list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_odd = 0

for num in numbers:
    if num % 2 != 0:
        sum_odd = sum_odd+num

print("Sum of odd numbers in the list:", sum_odd)

# Example 2: Using while loop
# Python program to find the sum of all odd numbers in a given list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_odd = 0
i = 0

while(i < len(numbers)):
    if numbers[i] % 2 != 0:
        sum_odd = sum_odd+numbers[i]
    i = i+1

print("Sum of odd numbers in the list:", sum_odd)

# Daily Challenge: Sum of Positive Numbers:

# Given a list of numbers, write a Python program to find the sum of all positive numbers in the list.
# Example 1: Using for loop
# Python program to find the sum of all positive numbers in a given list

numbers = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
sum_positive = 0

for num in numbers:
    if num > 0:
        sum_positive = sum_positive+num # sum_positive += num

print("Sum of positive numbers in the list:", sum_positive)

# Example 2: Using while loop

# Python program to find the sum of all positive numbers in a given list

numbers = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
sum_positive = 0
i = 0

while(i < len(numbers)):
    if numbers[i] > 0:
        sum_positive = sum_positive+numbers[i]
    i = i+1

print("Sum of positive numbers in the list:", sum_positive)

# Daily Challenge: Sum of Negative Numbers:

# Given a list of numbers, write a Python program to find the sum of all negative numbers in the list.
# Example 1: Using for loop
# Python program to find the sum of all negative numbers in a given list

numbers = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
sum_negative = 0

for num in numbers:
    if num < 0:
        sum_negative = sum_negative+num

print("Sum of negative numbers in the list:", sum_negative)

# Example 2: Using while loop
# Python program to find the sum of all negative numbers in a given list

numbers = [-1, 2, -3, 4, 5, 6, -7, 8, 9]

sum_negative = 0
i = 0

while(i < len(numbers)):
    if numbers[i] < 0:
        sum_negative = sum_negative+numbers[i]
    i = i+1

print("Sum of negative numbers in the list:", sum_negative)

