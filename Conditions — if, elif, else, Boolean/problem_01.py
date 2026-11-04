# Problem 11 — জোড় না বিজোড় একটি integer জোড় নাকি বিজোড় তা নির্ধারণ করো।


number = int(input("Enter number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")