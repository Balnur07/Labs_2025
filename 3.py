import re

f = open("input.txt", "r")
text = f.read()

x = re.findall("[a-z]+_[a-z]+", text)
print(x)