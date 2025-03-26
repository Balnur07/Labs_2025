st = str(input())
upper1 = 0
lower1 = 0
for i in st:
    if i.isupper():
        upper1+=1
    if i.islower():
        lower1+=1
print('lower:', lower1)
print('upper', upper1)