import re
def camel_to_snake(camel_str):
    snake_str = re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', camel_str)
    return snake_str.lower()
camel_string = str(input())
snake_string = camel_to_snake(camel_string)
print("Camel case:", camel_string)
print("Snake case:", snake_string)