# Problem 24 — Factorial একটি non-negative integer-এর factorial বের করো। ০! = ১ নিশ্চিত করো।

factorialNumber = int(input("Enter number: "))
factorial = 1
for i in range(1, factorialNumber + 1):
    factorial *= i

print(factorial)