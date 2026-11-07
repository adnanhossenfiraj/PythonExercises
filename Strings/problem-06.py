# Problem 42 — Password strength checker দৈর্ঘ্য, uppercase, lowercase, digit ও special character-এর ভিত্তিতে password strength-এর সাধারণ মূল্যায়ন করো।

import string

password = input("Enter password: ")

has_number = any(char in string.digits for char in password)
has_lower = any(char in string.ascii_lowercase for char in password)
has_upper = any(char in string.ascii_uppercase for char in password)
has_special = any(char in string.punctuation for char in password)

if (
    len(password) >= 8
    and has_number
    and has_lower
    and has_upper
    and has_special
):
    print("Strong Password! ")
else:
    print(
        "Weak Password!"
    )