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
