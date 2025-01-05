# Day 3: Python Fundamentals

# While Loop
print("While Loop Example:")
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1

# File Handling: Writing to and Reading from a File
print("\nFile Handling Example:")
file_name = "day3_sample.txt"

# Writing to the file
with open(file_name, "w") as file:
    file.write("This is Day 3 of Python Learning.\n")
    file.write("File handling is an essential skill!\n")

# Reading from the file
with open(file_name, "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# List Comprehensions
print("\nList Comprehensions:")
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print("Original List:", numbers)
print("Squared List:", squared_numbers)

# Basic Object-Oriented Programming (OOP)
print("\nOOP Example:")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I am {self.name} and I am {self.age} years old."

# Creating an object
person1 = Person("Sanjay", 20)
print(person1.introduce())

# Exception Handling
print("\nException Handling Example:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("This block always executes.")

# End of Day 3
print("\nKeep pushing forward!")
