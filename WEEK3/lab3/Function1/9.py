import math
def volume_sphere(r):
    V = (4/3) * math.pi * r**3
    return V

r = float(input("radius: "))
print (volume_sphere(r))
