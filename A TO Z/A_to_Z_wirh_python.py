"""  Here's a detailed A to Z Python guide with explanations and examples: """



"""A - Arithmetic Operations
Python supports basic arithmetic operators for mathematical calculations:

+: Addition
-: Subtraction
*: Multiplication
/: Division
%: Modulus (remainder)
**: Exponentiation
//: Floor Division (integer division)"""

a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333...
print(a % b)  # 1
print(a ** b) # 1000
print(a // b) # 3





"""B - Basic Input/Output
Python provides easy methods for taking input from the user and displaying output.

input() for user input.
print() for output """

name = input("What is your name? ")
print(f"Hello, {name}!")





"""C - Conditional Statements
Control the flow of your program using conditional statements like if, elif, and else.

Example: """

marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
else:
    print("Grade: C")





"""D - Data Types
Python has dynamic typing, so variables don't need explicit type definitions.

Common types: int, float, str, bool, list, tuple, dict, set
Example:

python """


age = 20          # int
height = 5.8      # float
name = "John"     # str
is_student = True # bool





"""E - Exception Handling
Python's try-except block lets you handle errors gracefully instead of crashing the program.

Example:"""

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")





"""F - Functions
Functions encapsulate reusable code. Use def to define a function.

Example:"""

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))




"""G - Generators
Generators create iterators that yield items lazily, saving memory compared to lists.

Example:"""

def count_up_to(n):
    for i in range(n):
        yield i

for num in count_up_to(5):
    print(num)





"""H - Higher-Order Functions
Functions like map(), filter(), and reduce() take other functions as arguments.

Example:"""

nums = [1, 2, 3]
squares = list(map(lambda x: x ** 2, nums))
print(squares)






"""I - Iterators
An iterator lets you traverse through all elements in a collection.

Example:"""

my_list = [1, 2, 3]
it = iter(my_list)
print(next(it))
print(next(it))






"""J - JSON Handling
JSON (JavaScript Object Notation) is widely used for data exchange in web applications.

Example:"""

import json

data = {"name": "John", "age": 30}
json_string = json.dumps(data)
print(json_string)

parsed_data = json.loads(json_string)
print(parsed_data["name"])





"""K - Keyword Arguments
Functions can take arguments by name, providing clarity and flexibility.

Example:"""

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(name="Alice", age=25)






"""L - Loops
Loops allow repetitive execution of code.

For loop: Iterates over items.
While loop: Runs until a condition is met.
Example:"""

for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1





"""M - Modules
Python libraries (modules) extend functionality, like math for mathematical operations.

Example:"""

import math

print(math.sqrt(16))
print(math.factorial(5))






"""N - NumPy Basics
NumPy is a library for numerical computing.

Supports multi-dimensional arrays and operations."""

import numpy as np

arr = np.array([1, 2, 3])
print(arr * 2)  # Element-wise multiplication






"""O - Object-Oriented Programming
Classes and objects allow structuring data and behavior.

Example:"""

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog = Dog("Buddy")
dog.bark()





"""P - Pandas Basics
Pandas is for data manipulation and analysis.

Example:"""

import pandas as pd

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df)





"""Q - Queue Handling
The queue module is useful for implementing FIFO or LIFO queues.

Example:"""

from queue import Queue

q = Queue()
q.put(1)
q.put(2)
print(q.get())





"""R - Recursion
Recursion is when a function calls itself.

Example:"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))




"""S - Strings
Python strings support numerous operations, such as formatting, slicing, and case conversion.

Example:"""

text = "Python"
print(text[0])         # P
print(text[::-1])      # nohtyP
print(text.upper())    # PYTHON





"""T - Try/Except
Handle exceptions to prevent program crashes.

Example:"""

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")




"""U - Unpacking
You can unpack elements of a list, tuple, or dictionary into variables.

Example:"""

a, b, c = [1, 2, 3]
print(a, b, c)




'''V - Virtual Environment
Virtual environments isolate Python projects, ensuring dependencies don't clash.

Create: python -m venv env
Activate:
Windows: env\Scripts\activate
Linux/Mac: source env/bin/activate'''




'''W - Web Scraping
Libraries like requests and BeautifulSoup help scrape web pages.

Example:'''

import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
soup = BeautifulSoup(response.content, "html.parser")
print(soup.title.text)




'''X - XML Parsing
The xml.etree.ElementTree module parses XML data.

Example:'''

import xml.etree.ElementTree as ET

data = "<root><child>Python</child></root>"
root = ET.fromstring(data)
print(root.find('child').text)




"""Y - Yield
Use yield in a function to create a generator.

Example:"""


def generate_numbers():
    for i in range(3):
        yield i

for num in generate_numbers():
    print(num)




"""Z - Zip
Combine two iterables into pairs.

Example:"""

names = ["Alice", "Bob"]
ages = [25, 30]
zipped = zip(names, ages)
print(list(zipped))  # [('Alice', 25), ('Bob', 30)]

