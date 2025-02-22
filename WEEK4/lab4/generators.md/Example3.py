def divisible(n):
    for i in range(0, n):
        if (i % 3 == 0 | i % 4 == 0):
            yield i

n = int(input("Input number: "))

for num in divisible(n):
    print(num)