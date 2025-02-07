def unique_elements(mylist):
    unique_list = []
    for item in mylist:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

mylist = input().split()
print(unique_elements(mylist))