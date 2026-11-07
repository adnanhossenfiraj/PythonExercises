# # Problem 40 — Word frequency একটি বাক্যে প্রতিটি শব্দ কতবার এসেছে তা dictionary-তে সংরক্ষণ করে দেখাও।

import string

text = """
Python is a powerful programming language. Python is easy to learn and Python is fun to use! 
Learning Python helps in data science, web development, and automation. Many developers love Python 
because Python has a clean syntax. Today, we are learning Python, coding in Python, and growing together!
"""

for p in string.punctuation:
    text = text.replace(p,"")

words = text.lower().split()
dictionary = {}

for word in words:
    dictionary[word] = dictionary.get(word, 0) +1


print(dictionary)