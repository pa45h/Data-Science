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
