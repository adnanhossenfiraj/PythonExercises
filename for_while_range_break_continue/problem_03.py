# Problem 23 — Multiplication table একটি সংখ্যার ১ থেকে ১০ পর্যন্ত নামতা দেখাও।

number = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{number} X {i} = {number * i}")