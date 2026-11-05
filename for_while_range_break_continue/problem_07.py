# Problem 27 — সংখ্যা উল্টানো একটি integer-এর digit উল্টে নতুন সংখ্যা তৈরি করো। leading zero হারিয়ে যাওয়ার বিষয়টি বিবেচনা করো।

original_number = int(input("Enter number: "))
reversed_str = str(original_number)[::-1]


print(int(reversed_str))