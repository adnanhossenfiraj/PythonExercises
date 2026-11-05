# Problem 30 — Fibonacci series Nটি Fibonacci সংখ্যা print করো। প্রথম কয়েকটি মান যাচাই করো।

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# F(n) = F(n-1) + F(n-2)


x= int(input("Enter number: "))
def get_nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(get_nth_fibonacci(x))  
