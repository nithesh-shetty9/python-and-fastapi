# Topic: Input and Output

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Name:", name)
print("Age:", age)
print(f"Hello {name}, you are {age} years old")


# Topic: Type Conversion

a = input("Enter first number: ")
b = input("Enter second number: ")

a = int(a)
b = int(b)

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)



# Topic: Arithmetic Operators

a = 15
b = 4

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Modulus
print(a ** b)  # Exponentiation



# Topic: Comparison Operators

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)



# Topic: Logical Operators (and, or, not)

age = 22
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)


# Topic: Membership and Identity Operators

numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 not in numbers)

x = None

print(x is None)
print(x is not None)

# Topic: if, elif, else

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")