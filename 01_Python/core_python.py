# More On : https://python.land/

# ========================= 01. PYTHON BASICS =========================

# Print something to the screen
print()
print("Hello, Python!")  # This is a single-line comment

"""
MULTI-LINE COMMENT
"""

# Variables and Data Types
name = "Parth"  # String
age = 20  # Integer
height = 5.9  # Float
is_student = True  # Boolean

# Type Checking
print(type(name), type(age), type(height), type(is_student))
print()

# ====================== 02. DATA TYPES & METHODS =====================


# String:
print("String:")
s = "  hello python  "

# Normal print: displays the string as-is (user-friendly) --> hello python
print("Normal print:", s)

# repr(): shows the string with quotes and visible whitespace (debug-friendly) --> '  hello python  '
print("Using repr():", repr(s))

print("Uppercase       :", s.upper())  # Converts to uppercase
print("Lowercase       :", s.lower())  # Converts to lowercase
print("Stripped        :", s.strip())  # Removes leading/trailing spaces
print("Replaced        :", s.replace("python", "world"))  # Replace substring
print("Split (default) :", s.split())  # Split by whitespace
print("Title Case      :", s.title())  # Capitalizes each word
print("Capitalize      :", s.capitalize())  # Capitalizes first letter
print("Starts with 'h' :", s.strip().startswith("h"))
print("Ends with 'n'   :", s.strip().endswith("n"))
print("Count of 'l'    :", s.count("l"))  # Count occurrences
print("Index of 'py'   :", s.find("py"))  # Find substring
print("Is Alpha        :", s.strip().isalpha())  # False, due to one space
print("Is Digit        :", s.isdigit())  # False, due to some chars
print("Is Lowercase    :", s.islower())  # True
print("Is Uppercase    :", s.isupper())  # False
print("Length          :", len(s))  # Total characters including spaces
print("Contains 'py'   :", "py" in s)  # Membership test
print()


# List:
print("List:")
# Initialize a list
my_list = [1, 2, 3]
print("Initial list:", my_list)

# Append adds a single element at the end
my_list.append(4)
print("After append(4):", my_list)

# Extend adds multiple elements at once
my_list.extend([5, 6])
print("After extend([5, 6]):", my_list)

# Remove deletes the first occurrence of the value
my_list.remove(2)
print("After remove(2):", my_list)

# Insert adds an element at a specific index
my_list.insert(1, 10)
print("After insert(1, 10):", my_list)

# Pop removes and returns the element at the given index (default: last)
last = my_list.pop()
print(f"After pop(): {my_list}", "→ popped element:", last)

# Index returns the first index of the given value
index_of_10 = my_list.index(10)
print("Index of 10:", index_of_10)

# Count returns number of occurrences of a value
count_3 = my_list.count(3)
print("Count of 3:", count_3)

# Sort arranges the list in ascending order
my_list.sort()
print("After sort():", my_list)

# Reverse reverses the order of elements
my_list.reverse()
print("After reverse():", my_list)

# Copy creates a shallow copy of the list
copied_list = my_list.copy()
print("Copied list:", copied_list)

# removes all elements
my_list.clear()
print("After clear():", my_list)
print()


# Tuple:
# Tuples are immutable – you cannot modify, append, or remove elements
print("Tuple:")
# Initialize a tuple
my_tuple = (1, 2, 3)
print("Initial tuple:", my_tuple)

# count(): Returns the number of occurrences of a specified value
count_2 = my_tuple.count(2)
print("Count of 2:", count_2)

# index(): Returns the index of the first occurrence of a specified value
index_1 = my_tuple.index(1)
print("Index of 1:", index_1)

# The following operations will raise an error:
# my_tuple[0] = 10        # TypeError
# my_tuple.append(4)      # AttributeError
# my_tuple.remove(1)      # AttributeError
print()


# Set: (stores unique values only)
print("Set:")
# empty set
my_set = set()
print("Empty set:", my_set)

my_set = {1, 2, 2, 3}  # Duplicates like 2 will be automatically removed
print("Initial set (duplicates removed):", my_set)

# add(): Adds an element to the set
my_set.add(4)
print("After adding 4:", my_set)

# update(): Adds multiple elements (can be a list, tuple, or set)
my_set.update([5, 6])
print("After updating with [5, 6]:", my_set)

# remove(): Removes a specific element; raises KeyError if not found
my_set.remove(1)
print("After removing 1:", my_set)

# discard(): Removes an element if it exists; does nothing if not found
my_set.discard(10)
print("After discarding 10 (no error even if not present):", my_set)

# pop(): Removes and returns a random element
popped = my_set.pop()
print(f"Popped element: {popped}")
print("After popping one element:", my_set)

# clear(): Removes all elements from the set
my_set.clear()
print("After clearing the set:", my_set)
print()


# Dictionary: stores key-value pairs
print("Dictionary:")
my_dict = {"name": "Parth", "age": 20}
print("Initial dictionary:", my_dict)

# keys(): Returns all keys
print("Keys in dictionary:", my_dict.keys())

# values(): Returns all values
print("Values in dictionary:", my_dict.values())

# get(): Safely gets the value for a key (returns None if not found)
print("Get value of key 'name':", my_dict.get("name"))

# update(): Updates dictionary with new key-value pairs
my_dict.update({"age": 21, "city": "Vadodara"})
print("After update (age and city):", my_dict)

# pop(): Removes a key and returns its value
popped_value = my_dict.pop("city")
print("Popped 'city':", popped_value)
print("After popping 'city':", my_dict)

# items(): Returns a view object of (key, value) pairs
print("Dictionary items (key-value pairs):", my_dict.items())

# clear(): Removes all key-value pairs from the dictionary
my_dict.clear()
print("After clearing dictionary:", my_dict)
print()

# ====================== 03. OPERATORS & CONDITIONS ======================

# ---------- Arithmetic Operators ----------
a, b = 10, 3
print(f"a={a}, b={b}")

print("Arithmetic Operators:")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a**b)  # Exponentiation
print("a // b =", a // b)  # Floor Division
print()

# ---------- Comparison Operators ----------
x, y = 7, 10
print(f"x={x}, y={y}")

print("Comparison Operators:")
print("x == y:", x == y)  # Equal to
print("x != y:", x != y)  # Not equal to
print("x > y:", x > y)  # Greater than
print("x < y:", x < y)  # Less than
print("x >= y:", x >= y)  # Greater than or equal to
print("x <= y:", x <= y)  # Less than or equal to
print()

# ---------- Logical Operators ----------
p, q = True, False
print(f"p={p}, q={q}")

print("Logical Operators:")
print("p and q:", p and q)  # Logical AND
print("p or q:", p or q)  # Logical OR
print("not p:", not p)  # Logical NOT
print()

# ---------- Bitwise Operators ----------
m, n = 5, 3  # In binary: 101 and 011
print(f"m={bin(m)}, n={bin(n)}")

print("Bitwise Operators:")
print("m & n =", m & n)  # AND
print("m | n =", m | n)  # OR
print("m ^ n =", m ^ n)  # XOR
print("~m =", ~m)  # NOT
print("m << 1 =", m << 1)  # Left Shift
print("m >> 1 =", m >> 1)  # Right Shift
print()

# ---------- Assignment Operators ----------
z = 5
print(f"z={z}")
print("Assignment Operators:")
z += 3
print("z += 3:", z)
z -= 2
print("z -= 2:", z)
z *= 4
print("z *= 4:", z)
z /= 2
print("z /= 2:", z)
z %= 5
print("z %= 5:", z)
z **= 2
print("z **= 2:", z)
z //= 2
print("z //= 2:", z)
print()

# ---------- Membership Operators ----------
nums = [1, 2, 3, 4]
print("nums =", nums)
print("Membership Operators:")
print("2 in nums:", 2 in nums)
print("5 not in nums:", 5 not in nums)
print()

# ---------- Identity Operators ----------
a1 = [10]
b1 = a1
c1 = [10]
print(f"a1={a1}, b1={b1},c1={c1}")
print("Identity Operators:")
print("a1 is b1:", a1 is b1)  # True - same object(memory location)
print(
    "a1 is c1:", a1 is c1
)  # False - different object(memory location) with same content
print("a1 == c1:", a1 == c1)  # True - same content
print()

# ---------- Conditional Statements ----------
age = 17
print("Conditional Statements:")
print(f"age={age}")
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
print()


# =========================== 04. LOOPS ===============================

print("=== For Loop ===")
# For loop: commonly used for iterating over a range or sequence
for i in range(5):  # 0 to 4
    print("Value from range:", i)

# Printing all items in a shopping cart
cart = ["Apples", "Bananas", "Oranges"]
for item in cart:
    print("Cart item:", item)


print("\n=== While Loop ===")
# While loop: repeats as long as a condition is True
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# Retry connection attempts (max 3 times)
print("\nSimulating connection attempts:")
attempt = 1
connected = False
while attempt <= 3 and not connected:
    print(f"Attempt {attempt}: trying to connect...")
    # Simulating failure for first 2 attempts
    if attempt == 3:
        connected = True
        print("Connected successfully!")
    attempt += 1


print("\n=== Loop Control Statements ===")
# continue: skip current iteration
# break: exit the loop

print("Using continue and break:")
for i in range(6):
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking at 5")
        break
    print("i:", i)


# pass: a placeholder when no code is needed
print("\nUsing pass (does nothing):")
for i in range(3):
    if i == 1:
        pass  # No operation
    print("Processing i:", i)


print("=== Loop with ELSE ===")
# FOR loop with else: executes else if loop completes without break
for i in range(5):
    print("i =", i)
else:
    print("For loop completed without break.\n")


# WHILE loop with else
x = 0
while x < 3:
    print("x =", x)
    x += 1
else:
    print("While loop ended normally.\n")


# Loop with else and break
for i in range(5):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)
else:
    print("This won't print because loop was broken.\n")
print()

print("=== Loop Comprehensions ===")
# List comprehension
squares = [x**2 for x in range(5)]
print("Squares (List):", squares)

# Set comprehension
unique_lengths = {len(word) for word in ["apple", "banana", "kiwi"]}
print("Set of word lengths:", unique_lengths)

# Dictionary comprehension
square_dict = {x: x**2 for x in range(4)}
print("Squares (Dict):", square_dict)

# Conditional comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)
print()


# ========================== 05. FUNCTIONS =============================

# 1. Basic Function
print("==== Functions ==== ")


def greet(name):
    return f"Hello, {name}!"


print(greet("Parth"))  # Hello, Parth!
print()


# 2. Function with Default Argument
def describe(name, age=18):
    print(f"{name} is {age} years old.")


describe("Parth")  # Default age
describe("pa45h", age=20)  # Custom age
print()

# 3. Keyword Arguments
describe(age=21, name="Jay")  # Order doesn't matter
print()


# 4. Variable-length Arguments (*args)
def print_fruits(*fruits):
    print("You like:")
    for fruit in fruits:
        print(fruit)


print_fruits("Apple", "Banana", "Cherry")
print_fruits("Apple", "Banana", "Cherry", "Apple", "Banana", "Cherry")
print()


# 5. Variable-length Keyword Arguments (**kwargs)
def student_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


student_details(name="Parth", age=20, branch="CE")
print()

# 6. Lambda (Anonymous) Function
square = lambda x: x**2
print("Square of 5 is:", square(5))
print()


# 7. Passing Function as Argument
def apply_operation(func, value):
    return func(value)


print("Cube using lambda:", apply_operation(lambda x: x**3, 3))
print()


# 8. Nested Function
def outer():
    def inner():
        print("Inner function called")

    print("Calling inner from outer:")
    inner()


outer()

print()


# 9. Return Multiple Values
def min_max(numbers):
    return min(numbers), max(numbers)


mn, mx = min_max([3, 7, 1, 9])
print("Min:", mn, "Max:", mx)
print()


# 10. Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of 5 is:", factorial(5))
print()

# 11. Higher-order Functions: map, filter, reduce:
nums = [1, 2, 3, 4, 5]
print(f"nums{nums}")
# map: square each number
squares = list(map(lambda x: x**2, nums))
print("Squares using map:", squares)
print()

# filter: even numbers only
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers using filter:", evens)
print()

# reduce: product of all numbers
from functools import reduce

product = reduce(lambda x, y: x * y, nums)
print("Product using reduce:", product)
print()


# ====================== 06. DATA STRUCTURES ===========================
print("==== DATA STRUCTURES ====")
# === Stack (LIFO: Last In, First Out) using list ===
stack = []  # Initialize empty stack
stack.append(1)  # Push 1 onto the stack
stack.append(2)  # Push 2 onto the stack
print(stack)  # Output: [1, 2]
stack.pop()  # Pop (remove and return) the top element (2)
print(stack)  # Output: [1]
print()

# === Queue (FIFO: First In, First Out) using collections.deque ===
from collections import deque

queue = deque([1, 2])  # Initialize queue with 1 and 2
queue.append(3)  # Enqueue 3 at the end
print(queue)  # Output: deque([1, 2, 3])
queue.popleft()  # Dequeue (remove and return) element from front (1)
print(queue)  # Output: deque([2, 3])
print()

# === Set: Unordered collection of unique items ===
my_set = {1, 2, 3}
my_set.add(4)  # Add an element
my_set.discard(2)  # Remove element if present
print(my_set)  # Output: {1, 3, 4}
print()

# === Dictionary: Key-value pairs ===
my_dict = {"name": "Parth", "age": 20}
print(my_dict["name"])  # Access value by key
my_dict["age"] = 21  # Update value
my_dict["city"] = "Vadodara"  # Add new key-value pair
print(my_dict)
print()

# === Tuple: Immutable ordered collection ===
my_tuple = (10, 20, 30)
print(my_tuple[1])  # Access element by index
# my_tuple[0] = 5  →  Error: Tuples are immutable
print()

# === List: Ordered, mutable collection ===
my_list = [1, 2, 3]
my_list.append(4)  # Add element at end
my_list.remove(2)  # Remove specific element
print(my_list)  # Output: [1, 3, 4]
print()


# ===================== 07. FILE HANDLING ==============================
print("==== FILE HANDLING ====")
# === Write to a file (creates new or overwrites if file exists) ===
with open("example.txt", "w") as f:
    f.write("Hello File!\nThis is a new line.")
print("[Write] Wrote to 'example.txt'")
print()

# === Read entire content from a file ===
with open("example.txt", "r") as f:
    content = f.read()
print("[Read] File content:\n", content)
print()

# === Append to the file without overwriting existing content ===
with open("example.txt", "a") as f:
    f.write("\nAppending a new line.")
print("[Append] Appended text to 'example.txt'")
print()

# === Read file line by line using readline() ===
with open("example.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
print("[Readline] First Line:", line1.strip())
print("[Readline] Second Line:", line2.strip())
print("[Readline] Third Line:", line3.strip())
print("[Readline] Fourth Line:", line4.strip())
print()

# === Read all lines as a list using readlines() ===
with open("example.txt", "r") as f:
    lines = f.readlines()
print("[Readlines] All lines as list:", lines)
print()

# === Write multiple lines using writelines() ===
lines_to_write = ["Line A\n", "Line B\n", "Line C\n"]
with open("example2.txt", "w") as f:
    f.writelines(lines_to_write)
print("[Writelines] Multiple lines written to 'example2.txt'")
print()

# === File exists check before reading (good practice) ===
import os

filename = "example3.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f"[Exists] {filename} content:\n", f.read())
else:
    print(f"[Exists] {filename} does not exist.")
print()
# === Using 'with' ensures file is automatically closed after use ===


# ===================== 08. ERROR HANDLING =============================
print("==== ERROR HANDLING ====")
# === Basic try-except-finally example ===
try:
    val = 10 / 0
except ZeroDivisionError:
    print("[Error] Cannot divide by zero!")
finally:
    print("[Finally] This always runs.")
print()

# === Catching multiple exception types ===
try:
    num = int("abc")  # ValueError
except ValueError:
    print("[Error] Invalid conversion to integer.")
except TypeError:
    print("[Error] Type mismatch.")
print()

# === Using else block: runs if no exception occurs ===
try:
    result = 10 / 2
except ZeroDivisionError:
    print("[Error] Division by zero.")
else:
    print("[Else] Division successful. Result =", result)
print()

# === Catching all exceptions generally (not recommended for production) ===
try:
    print(undefined_variable)  # type: ignore # NameError
except Exception as e:
    print("[General Exception] An error occurred:", e)
print()


# === Raising custom exceptions ===
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount


try:
    new_balance = withdraw(1000, 1500)
except ValueError as e:
    print("[Custom Error] Withdrawal failed:", e)
print()


# === Custom Exception class ===
class MyError(Exception):
    pass


try:
    raise MyError("Something custom went wrong!")
except MyError as e:
    print("[Custom Exception Class] Caught:", e)
print()

# ====================== 09. OBJECT ORIENTED ===========================
print("==== OBJECT ORIENTED ====")


# === Basic Class with Constructor and Instance Method ===
class Person:
    def __init__(self, name):  # Constructor
        self.name = name  # Instance attribute

    def greet(self):  # Instance method
        print(f"Hi, I'm {self.name}")


p = Person("Parth")
p.greet()  # Output: Hi, I'm Parth
print()


# === Inheritance ===
class Student(Person):  # Student inherits from Person
    def study(self):
        print("Studying...")


s = Student("Part Katariya")
s.greet()  # Inherited method
s.study()  # Student-specific method
print()


# === Method Overriding ===
class Teacher(Person):
    def greet(self):  # Override greet()
        print(f"Hello, I'm Prof. {self.name}")


t = Teacher("Ankita")
t.greet()  # Output: Hello, I'm Prof. Ankita
print()


# === Encapsulation (Public, Protected, Private) ===
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Public
        self._balance = balance  # Protected
        self.__pin = "1234"  # Private

    def show_balance(self):
        print(f"Balance: ₹{self._balance}")

    def __show_pin(self):  # Private method
        print(f"PIN: {self.__pin}")


acct = BankAccount("Ravi", 5000)
acct.show_balance()  #  Access public method
print(acct.owner)  #  Public
print(acct._balance)  #  Accessing protected (allowed but not recommended)
# print(acct.__pin)          #  Error: Private attribute
# acct.__show_pin()          #  Error: Private method
print()


# === Polymorphism (same interface, different behavior) ===
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


def make_sound(animal):
    animal.sound()  # Polymorphic behavior


make_sound(Dog())  # Output: Bark
make_sound(Cat())  # Output: Meow
print()


# === Class Method and Static Method ===
class Circle:
    pi = 3.1415

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @staticmethod
    def unit_circle_area():
        return Circle.pi * 1 * 1


c1 = Circle.from_diameter(10)
print("Radius from diameter:", c1.radius)  # 5.0

print("Area of unit circle:", Circle.unit_circle_area())  # 3.1415
print()

# ====================== 10. ADVANCED TOPICS ===========================

# Decorators allow behavior to be added to a function dynamically.
print("==== DECORATOR ====")


def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@decorator
def say_hi():
    print("Hi!")


say_hi()
print()


# Generators allow you to iterate over values lazily using 'yield'.
print("==== GENERATOR ====")


def generate_nums():
    for i in range(3):
        yield i


print(generate_nums())
for num in generate_nums():
    print(num)
print()

# ================= MULTITHREADING & MULTIPROCESSING =================
print("==== MULTITHREADING ====")
# Threading for running tasks in parallel (for I/O-bound tasks).
import threading
import time


# A CPU heavy calculation, just as an example. This can be anything you like
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, " is done")


def threaded(n):
    threads = []
    for i in range(n):
        t = threading.Thread(
            target=heavy,
            args=(
                500,
                i,
            ),
        )
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    start = time.time()
    threaded(80)
    end = time.time()
    print("Took: ", end - start)
print()


print("==== MULTIPROCESSING ====")
import time
import multiprocessing

# A CPU heavy calculation, just
# as an example. This can be
# anything you like
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, "is done")


def multiproc(n):
    processes = []
    for i in range(n):
        p = multiprocessing.Process(
            target=heavy,
            args=(
                500,
                i,
            ),
        )
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


if __name__ == "__main__":
    start = time.time()
    multiproc(80)
    end = time.time()
    print("Took: ", end - start)
print()


# ========================= ASYNC / AWAIT ============================
print("==== ASYNC / AWAIT ====")
# Async IO allows concurrent execution of IO-bound operations.
import asyncio


async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


asyncio.run(greet())
print()


# =================== MODULES AND PACKAGES ===========================
print("==== MODULES AND PACKAGES ====")
# Importing a standard module.
import math

print(math.sqrt(16))  # Using math module to get square root

# Custom modules are your own Python files you can import and reuse.
print()


# =================== MEMORY MANAGEMENT ==============================
print("==== MEMORY MANAGEMENT ====")
import sys
import gc

x = [1, 2, 3, 4, 5]
print(sys.getsizeof(x))  # Get memory size of object

gc.collect()  # Force garbage collection
print()


# ================= TYPE HINTS / ANNOTATIONS =========================
print("==== TYPE HINTS / ANNOTATIONS ====")


def add(a: int, b: int) -> int:
    return a + b


print(add(3, 4))  # Helps with static type checking (e.g., using mypy)
print()


# ================== SERIALIZATION (Pickle / JSON) ===================
print("==== SERIALIZATION (Pickle / JSON) ====")
import pickle
import json

# Pickle: Python-specific serialization
obj = {"name": "Parth", "age": 20}
with open("data.pkl", "wb") as f:
    pickle.dump(obj, f)  # Serializing to binary

with open("data.pkl", "rb") as f:
    data = pickle.load(f)
    print("pickle =", data)

# JSON: Language-independent serialization
json_data = json.dumps(obj)  # Convert dict to JSON string
print("json =", json_data)
print()


# ================== ENVIRONMENT VARIABLES ============================
print("==== ENVIRONMENT VARIABLES ====")
import os

os.environ["MY_ENV"] = "value"  # Setting an env variable
print(os.getenv("MY_ENV"))  # Accessing env variable
print()


# ================= PROFILING / PERFORMANCE ===========================
print("==== PROFILING / PERFORMANCE ====")

import time

# Simple timing using time.time()
start = time.time()

# Sum of first 10 million numbers (large enough to notice time, but not crash system)
sum_result = 0
for i in range(10_000_000):
    sum_result += i

end = time.time()

print("Execution Time using time.time():", end - start, "seconds\n")

# Advanced profiling using cProfile
import cProfile


# Function to compute sum using built-in range and sum (more efficient)
def compute():
    total = sum(range(1000))
    return total


# Profile the function using cProfile
print("Profiling using cProfile:")
cProfile.run("compute()")
print()
