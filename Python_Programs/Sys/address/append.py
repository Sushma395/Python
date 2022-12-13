from address import a,b
import sys
print(f"b : {b}")
for i in b:
    print(f"id :{id(i)} size: {sys.getsizeof(i)}")
a.extend([7, 8, 9, 10])
print(f"a after append: {a}")
for i in a:
    print(f"id :{id(i)} size: {sys.getsizeof(i)}")
