import sys
# get id of list
a = [1, 2, 3, 4, 5]
b = [13, 14, 15]
a.extend([7, 8, 9, 10, 11, 12])
b.append(16)
print(f"Address of a: {a}")
for i in a:
    print(f"id :{id(i)} size: {sys.getsizeof(i)}")
print(f"Address of b: {b}")
for j in b:
    print(f"id :{id(j)} size: {sys.getsizeof(j)}")
