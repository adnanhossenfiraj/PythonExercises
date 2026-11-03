# Problem 09 — অদলবদল দুটি variable-এর মান তৃতীয় variable ব্যবহার করে এবং পরে Python-এর tuple unpacking দিয়ে অদলবদল করো।

a = 10
b = 20
print(f"first: a:{a}, b:{b}")

temp = a
a = b
b = temp
print(f"temp: a:{a}, b:{b}")

a = 10
b = 20
a, b = b, a
print(f"unpacking: a:{a}, b:{b}")