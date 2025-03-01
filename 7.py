def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    camel_case = parts[0] + ''.join(word.capitalize() for word in parts[1:])
    return camel_case
snake_string =str(input())
camel_string = snake_to_camel(snake_string)
print("Snake case:", snake_string)
print("Camel case:", camel_string)