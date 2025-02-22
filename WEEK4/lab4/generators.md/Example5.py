def kersinshe(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Input number: "))        

for num in kersinshe(n):
    print(num)