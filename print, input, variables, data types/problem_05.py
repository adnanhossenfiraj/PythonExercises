# Problem 05 — আয়তক্ষেত্রের হিসাব দৈর্ঘ্য ও প্রস্থ input নিয়ে ক্ষেত্রফল এবং পরিসীমা বের করো।

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area}\nPerimeter: {perimeter}")
