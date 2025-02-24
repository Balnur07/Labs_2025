import re

text = str(input())
x = re.findall("[A-Z][^A-Z]*", text)
print("Original string:", text)
print("Split parts:", x)