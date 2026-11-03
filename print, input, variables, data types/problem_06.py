# Problem 06 — বৃত্তের হিসাব ব্যাসার্ধ input নিয়ে বৃত্তের ক্ষেত্রফল ও পরিধি বের করো।


radius = float(input("Enter radius: "))

pi = 3.141592653589793
area = pi * radius**2
circumference = 2 * (pi * radius)

print(f"Area: {area}")
print(f"Circumference: {circumference}")