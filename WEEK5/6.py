import re

f = open("input.txt", "r")
text = f.read()

x = re.sub("\s", ",", text)
print(x)