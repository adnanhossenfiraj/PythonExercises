# Problem 26 — অঙ্কগুলোর যোগফল একটি integer-এর digit-গুলোর যোগফল বের করো।

number = int(input("Enter number: "))
# number = 12
strNmuber = str(number)
totalSum = 0

for i in range(len(strNmuber)):
    numberSlice = strNmuber[i]
    intNumber = int(numberSlice)
    totalSum += intNumber

print("Total:",totalSum)