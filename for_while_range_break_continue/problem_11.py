# Problem 31 — সব divisor একটি সংখ্যার সব ধনাত্মক divisor বের করো।

number = int(input("Enter number: "))
divisor = []

for i in range(1, number + 1):
    if number % i == 0:
        divisor.append(i)


print(divisor)