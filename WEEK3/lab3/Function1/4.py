def prime_num(n):
    for i in range(n):
        if n % i != 0:
            continue
        else:
            return i
        
n = int(input())
print(prime_num(n))        