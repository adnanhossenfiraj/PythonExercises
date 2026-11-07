# Problem 39 — Palindrome string space ও punctuation উপেক্ষা করে একটি শব্দ/বাক্য palindrome কি না পরীক্ষা করো।

import string

text = "Madam"
cleaned_text = text

for p in string.punctuation:
  cleaned_text = cleaned_text.replace(p, "").replace(" ", "").lower()

repText = cleaned_text[::-1]

if cleaned_text == repText:
  print("this text is palindrome")
else:
  print("this text is not palindrome")