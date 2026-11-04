# Problem 16 — বয়স অনুযায়ী শ্রেণি বয়স অনুযায়ী শিশু, কিশোর, প্রাপ্তবয়স্ক বা প্রবীণ শ্রেণি দেখাও। সীমার মানগুলো পরিষ্কারভাবে নির্ধারণ করো।

# 0 - 12 Child
# 13 – 17 Adolescent
# 18 - 59 Adult
# age => 60 Older Person

try:
    age = int(input("Enter your age: "))
except Exception:
    print("Error: please enter correct age")
    exit()



if age < 0:
    print("Please enter correct age")
    
elif 0 <= age <= 12:
    print("Child group")

elif 13 <= age <= 17:
    print("Adolescent group")

elif 18 <= age <= 59:
    print("Adult group")

else:  # age >= 60
    print("Older person")