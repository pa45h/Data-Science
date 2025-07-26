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
