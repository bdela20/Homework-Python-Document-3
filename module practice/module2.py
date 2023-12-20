from math import pi
def circ_circumference(r):
    return round(2 * pi * radius, 2)
radius = float(input("Radius: "))
circumference = circ_circumference(radius)
print("Circumference: " + str(circumference))


