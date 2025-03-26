import re

f = open("input.txt", "r")
text = f.read()

x = re.findall("[A-Z][a-z]+", text)
print(x)