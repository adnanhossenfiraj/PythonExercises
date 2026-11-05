# Problem 32 — GCD ও LCM দুটি integer-এর GCD এবং LCM বের করো; সম্ভব হলে Euclidean algorithm ব্যবহার করো।


def find_gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def find_lcm(a: int, b: int):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // find_gcd(a, b)


if __name__ == "__main__":
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    
    gcd_result = find_gcd(num1, num2)
    lcm_result = find_lcm(num1, num2)
    
    print(f"Numbers: {num1} & {num2}")
    print(f"GCD: {gcd_result}")
    print(f"LCM: {lcm_result}")