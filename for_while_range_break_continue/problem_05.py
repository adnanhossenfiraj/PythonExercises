# Problem 25 — Digit count একটি integer-এ মোট কয়টি digit আছে তা বের করো; শূন্যের ক্ষেত্রটিও পরীক্ষা করো।

number = input("Enter number: ")
intNumber = int(number)


digit = "Total number with zero {} and without zero {}"
if len(number) != len(str(intNumber)):
    print(digit.format(len(number), len(str(intNumber))))
else:
    print(f"Total digit: {len(str(intNumber))}")
