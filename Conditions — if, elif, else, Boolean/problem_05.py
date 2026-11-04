# Problem 15 — পরীক্ষার Grade নম্বর input নিয়ে নির্ধারিত scale অনুযায়ী grade দেখাও; ০–১০০-এর বাইরে input প্রত্যাখ্যান করো।

# Academic grading in the United States
# Grade    Percentage	GPA
# A+    	97–100% 	4.0
# A	        93–96%  	3.9
# A−    	90–92%  	3.7
# B+    	87–89%  	3.3
# B	        83–86%  	3.0
# B−    	80–82%  	2.7
# C+    	77–79%  	2.3
# C       	73–76%  	2.0
# C−    	70–72%  	1.7
# D+    	67–69%  	1.3
# D	        63–66%  	1.0
# D−    	60–62%  	0.7
# F     	0–59%   	0.0

try:
    number = float(input("Enter your marks: "))
except ValueError:
    print("Please enter a valid number!")
    exit()

if 0 <= number <= 100:
    if 97 <= number <= 100:
        print("Grade: A+")

    elif 93 <= number <= 96:
        print("Grade: A")

    elif 90 <= number <= 92:
        print("Grade: A-")

    elif 87 <= number <= 89:
        print("Grade: B+")

    elif 83 <= number <= 86:
        print("Grade: B")

    elif 80 <= number <= 82:
        print("Grade: B-")

    elif 77 <= number <= 79:
        print("Grade: C+")

    elif 73 <= number <= 76:
        print("Grade: C")

    elif 70 <= number <= 72:
        print("Grade: C-")

    elif 67 <= number <= 69:
        print("Grade: D+")

    elif 63 <= number <= 66:
        print("Grade: D")

    elif 60 <= number <= 62:
        print("Grade: D-")
        
    else:
        print("Grade: F")
else:
    print("Please enter a correct number between 0 and 100!")