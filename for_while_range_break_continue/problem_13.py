# Problem 33 — Pattern printing N input নিয়ে তারকা (*) দিয়ে right triangle, pyramid ও উল্টো triangle pattern তৈরি করো।

# number = int(input("Enter number: "))
number = 10

print("right triangle")
for i in range(1, number + 1):
    spc = " " * (number - i)
    star = "*" * i
    print(spc, star)

print("Inverted right triangle")
for i in range(number + 1):
    star = "*" * (number - i)
    spc = " " * i
    print(spc, star)

print("left triangle")
for i in range(1, number + 1):
    spc = " " * (number - i)
    star = "*" * i
    print(star, spc)

print("Inverted left triangle")
for i in range(number + 1):
    star = "*" * (number - i)
    spc = " " * i
    print(star, spc)

print("pyramid")
for i in range(1, number + 1):
    spc = " " * (number - i)
    star = "* " * i
    print(spc, star)

print("Inverted pyramid")
for i in range(number + 1):
    star = " *" * (number - i)
    spc = " " * i
    print(spc, star)
