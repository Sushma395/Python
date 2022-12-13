# To find remainder of array elements multiplication - divided by n

arr = [100, 10, 5, 25, 35, 14]
print(f"Array: {arr}")
ln = len(arr)
n = int(input("Divide by num after multiplying all the elements:"))
m = 1
for i in range(0, ln):
    m *= arr[i]
print(f"Remainder of array elements multiplication - divided by num n: {m % n}")