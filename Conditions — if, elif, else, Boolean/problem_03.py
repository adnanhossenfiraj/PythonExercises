# Problem 13 — তিন সংখ্যার মধ্যে বড় তিনটি সংখ্যা input নিয়ে সবচেয়ে বড়টি বের করো। built-in max() ছাড়াও একবার চেষ্টা করো।

number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))
number3 = int(input("Enter 3rd number: "))

if number1 >= number2 and number1 >= number3:
    print(f"{number1} is the biggest")

elif number2 >= number1 and number2 >= number3:
    print(f"{number2} is the biggest")

else:
    print(f"{number3} is the biggest")