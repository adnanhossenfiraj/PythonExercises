# Problem 04 — চারটি গাণিতিক কাজ দুটি সংখ্যার যোগ, বিয়োগ, গুণ ও ভাগফল দেখাও। শূন্য দিয়ে ভাগের বিষয়টি সামলাও।

number1 = int(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
number2 = int(input("Enter second number: "))

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    if number2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(number1 / number2)
else:
    print("Please enter a correct operator (+, -, *, /)!")
