def slow_function_1():
    total = 0
    for i in range(1, 10_000_001):
        total += i
    print("Total (slow):", total)


def fast_function_1():
    n = 10_000_000
    total = n * (n + 1) // 2
    print("Total (fast):", total)


for i in range(0, 5):
    slow_function_1()
    fast_function_1()


a = 1 / 0
FILE_PATH = "C:\UERS\DSCD\CD.CD"

for i in range(10):
    b = open(FILE_PATH + f"\{i}.txt", "r")
    content = b.read()
    c = open("C:\Users\copy\{i}.txt", "w")
    c.write(content)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

data = [1, 2, 3, 4, 5]
if 4 in data:
    print("Found!")
