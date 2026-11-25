# Topic: Modulus Operator and if-else

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Topic: Comparison Operators and if-elif-else

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# Topic: Conditional Statements

num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



    # Topic: Conditional Statements and Arithmetic Operators

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# Topic: if-elif-else and Arithmetic Operators

units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 2
    print("Electricity Bill: ₹", bill)
elif units <= 200:
    bill = 100 * 2 + (units - 100) * 3
    print("Electricity Bill: ₹", bill)
elif units <= 500:
    bill = 100 * 2 + 100 * 3 + (units - 200) * 5
    print("Electricity Bill: ₹", bill)
else:
    bill = 100 * 2 + 100 * 3 + 300 * 5 + (units - 500) * 8
    print("Electricity Bill: ₹", bill)


# Topic: Input, Type Conversion, Arithmetic and Conditional Statements

name = input("Enter student name: ")

m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))

if 0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100:
    total = m1 + m2 + m3
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Student:", name)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)
else:
    print("Invalid marks! Enter values between 0 and 100.")

