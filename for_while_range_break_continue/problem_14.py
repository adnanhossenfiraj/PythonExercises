# Problem 34 — Guess the number কম্পিউটার একটি নির্দিষ্ট সংখ্যা রাখবে; ব্যবহারকারী অনুমান করবে এবং “বড়/ছোট” hint পাবে। চেষ্টা সংখ্যা গণনা করো।


import random

randomNumber = random.randint(1, 100)
number = randomNumber
userTry = 0

while True:
    userNumber = int(input("Enter number (1-100): "))
    userTry += 1
    
    if userNumber > number:
        print(f"{userNumber} is too high")
    elif userNumber < number:
        print(f"{userNumber} is too low")
    else:
        print(f"Congratulations! You guessed the correct number {userNumber} in {userTry} attempts.")
        break
