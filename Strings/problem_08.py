# Problem 44 — Duplicate character একটি string-এ কোন character একাধিকবার এসেছে এবং কতবার এসেছে তা দেখাও।


import string

character = "Learning Python is Fun! Today is Saturday, and we are coding together."

for p in string.punctuation:
    character = character.replace(p,"").replace(" ", "").lower()


total = ""
for char in set(character):
    count = character.count(char)
    total += f"{char} is {count}\n"


print(total)
