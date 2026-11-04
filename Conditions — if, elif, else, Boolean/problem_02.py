# Problem 12 — ধনাত্মক, ঋণাত্মক নাকি শূন্য একটি সংখ্যা পরীক্ষা করে তিনটির মধ্যে সঠিক ফল দেখাও।

number = int(input("Enter number: "))

if number == 0:
    print(f"{number} is zero")

elif number > 0:
    print(f"{number} is positive")
    
else:
    print(f"{number} is negative")