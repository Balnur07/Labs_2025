def even_num(n):

    for i in range(0, n + 1, 2):
     yield i

n = int(input("san engiz: "))    

for num in even_num(n):
    print(num)