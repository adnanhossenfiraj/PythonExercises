# Problem 22 — যোগফল N input নিয়ে ১ থেকে N পর্যন্ত সংখ্যার যোগফল loop দিয়ে বের করো।

number = int(input("Enter number: "))
total = 0

for i in range(1,number+1):
    total += i

print("sum:",total)