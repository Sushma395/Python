def sum_c(n):
    c = 0
    for i in range(1, n+1):
        c += i**3
    return c


n = int(input("Enter num to find sum of squares, cubes:"))
print(f"Sum of squares is: {sum(i**2 for i in range(1, n+1))}")
print(f"Sum of cubes is: {sum_c(n)}")
