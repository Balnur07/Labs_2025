import re

text = str(input("text: "))
x = re.findall("a.+b$", text)
print(x)