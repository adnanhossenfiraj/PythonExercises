# Problem 37 — Vowel counter ইংরেজি বাক্যে vowel কতটি আছে গণনা করো; uppercase ও lowercase উভয় সামলাও।

string = "Learning Python is Fun! Today is Saturday, and we are coding together."

vowel = ['a', 'e', 'i', 'o', 'u']
vowelCounter = 0

for i in string:
    if i.lower() in vowel:
        vowelCounter += 1


print(vowelCounter)