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
