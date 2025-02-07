def solve(heads, legs):
    y = (legs - 2 * heads) / 2
    x = heads - y
    return int(x), int(y)

heads = float(input("write (35): "))
legs = float(input("write (94): "))

x, y = solve(heads, legs)
print(x, y)