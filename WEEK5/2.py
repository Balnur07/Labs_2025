import re

f = open("input.txt", "r")
text = f.read()

x = re.findall(r"ab{2,3}", text)
print(x)