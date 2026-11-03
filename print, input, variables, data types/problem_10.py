# Problem 10 — সাধারণ বিল পণ্যের দাম ও পরিমাণ input নিয়ে মোট দাম, discount এবং চূড়ান্ত বিল বের করো।

# ১,০০০-এর কম	      ০% (কোনো discount নেই)
# ১,০০০ থেকে ৪,৯৯৯	   ৫%
# ৫,০০০ থেকে ৯,৯৯৯	   ১০%
# ১০,০০০ থেকে ১৯,৯৯৯   ১৫%
# ২০,০০০ বা তার বেশি	২০%


prod_Item = int(input("Enter total product: "))
totalPrice = 0

for i in range(prod_Item):
    price = int(input(f"Enter product {i+1} price: "))
    quantity = int(input(f"Enter product {i+1} quantity: "))
    if quantity > 0:
        totalPrice += price * quantity


if totalPrice >= 20000:
    dis = 20
elif totalPrice >= 10000:
    dis = 15
elif totalPrice >= 5000:
    dis = 10
elif totalPrice >= 1000:
    dis = 5
else:
    dis = 0

finalPrice = totalPrice - (dis / 100) * totalPrice

print(f"Total price: {totalPrice}")
print(f"Discount: {dis}%")
print(f"Final price: {finalPrice}")