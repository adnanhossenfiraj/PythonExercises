# Problem 35 — Input validation loop ব্যবহারকারী সঠিক range-এর সংখ্যা না দেওয়া পর্যন্ত input চাইতে থাকো। ভুল input-এ crash যেন না হয়।

import random

randomNumber = random.randint(1, 100)
number = randomNumber
userTry = 0

while True:
    try:
        userNumber = int(input("Enter number (1-100): "))
        if 1 <= userNumber <= 100:
            userTry += 1
            if userNumber > number:
                print(f"{userNumber} is too high")
            elif userNumber < number:
                print(f"{userNumber} is too low")
            else:
                print(f"Congratulations! You guessed the correct number {userNumber} in {userTry} attempts.")
                break
        else:
            print("Please enter a number between 1 and 100 only!")

    except ValueError:
        print("Please enter a valid integer only!")