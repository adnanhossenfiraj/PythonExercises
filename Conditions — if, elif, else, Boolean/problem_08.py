# Problem 18 — Simple calculator ব্যবহারকারীর বেছে নেওয়া operator (+, -, *, /) অনুযায়ী হিসাব করো। অবৈধ operator ও division by zero সামলাও।

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
