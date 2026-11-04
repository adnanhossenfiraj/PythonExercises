# Problem 14 — Leap year একটি বছর leap year কি না Gregorian calendar-এর নিয়ম অনুযায়ী নির্ধারণ করো।

year = int(input("Enter year: "))

leapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if leapYear:
    print(f"{year} is leap year")

else:
    print(f"{year} is not leap year")