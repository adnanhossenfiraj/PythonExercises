# Problem 08 — সেকেন্ডকে সময়ে রূপান্তর মোট সেকেন্ড input নিয়ে কত ঘণ্টা, মিনিট ও সেকেন্ড তা দেখাও।

try:
    sec = int(input("Enter seconds: "))

    if sec < 0:
        print("Seconds cannot be negative!")
    else:
        h = sec // 3600
        m = (sec % 3600) // 60
        s = sec % 60

        print(f"{h}H, {m}M, {s}S")

except ValueError:
    print("Please enter numbers only!")