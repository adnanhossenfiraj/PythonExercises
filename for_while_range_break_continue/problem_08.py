# Problem 28 — Palindrome number একটি সংখ্যা সামনে ও পেছন থেকে একই কি না পরীক্ষা করো।

number = input('Enter number')
# number = "1234321"

revNumber = number[::-1]

if number == revNumber:
    print(f"{number} this number is palindrome")
else:
    print(f"{number} this number is not palindrome")
    