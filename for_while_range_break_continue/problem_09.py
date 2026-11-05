# Problem 29 — Prime number একটি সংখ্যা prime কি না নির্ধারণ করো। ১ ও ঋণাত্মক সংখ্যার edge case সামলাও।

number = int(input("Enter number: "))
test = 1


if number > 1:
    for i in range(2, number):
        if number % i == 0:
            test = 0
            break
    print(f"{number} is not prime") if test == 0 else print(f"{number} is prime")


else:
    print(f"{number} is not a prime number")
