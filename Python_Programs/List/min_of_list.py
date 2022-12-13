lst1 = list(map(int, input("Enter list elements:").split()))
print(f"List is: {lst1}")
m = lst1[0]
for i in lst1:
    if i < m:
        m = i
print(f"Minimum of list: {m}")
# sort() or min() can be used
