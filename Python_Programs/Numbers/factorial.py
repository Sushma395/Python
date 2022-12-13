n = int(input("Enter num to find factorial:"))
if n < 0:
    fac = 0
elif n == 0 or n == 1:
    fac = 1
else:
    fac = 1
    for i in range(1, n+1):
        fac = fac*i
print(f"factorial of n is: {fac}")