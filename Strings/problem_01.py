# Problem 36 — String analysis একটি বাক্যে character, character বাদে space, word এবং line-এর সংখ্যা বের করো।

string = "Learning Python is Fun!\nToday is Saturday, and we are coding together."


character = len(string)

space = string.count(" ")

word = string.split()

line = string.count("\n") + 1


print(string,"\n")
print(f"character: {character}, space: {space}, word: {len(word)}, line: {line}")