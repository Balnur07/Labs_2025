import re

text = str(input())
x = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
print("Result:", x)