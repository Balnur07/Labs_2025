import re

f = open("input.txt", "r")
text = f.read()

x = re.findall(r"ab*", text)
print(x)
