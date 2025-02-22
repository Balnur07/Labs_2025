def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Number start: "))   
b = int(input("Number end: "))   

for num in squares(a, b):
    print(num)