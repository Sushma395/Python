# Area of triangle having 3 sides (Heron's formula)
a, b, c = map(float, input("Enter sides of triangle a b c:").split())
s = (a+b+c)/2 #semi perimeter
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"Area of triangle: {area}")



