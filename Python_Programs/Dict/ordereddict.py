# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict

print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
    print(key, value)

print("\nAfter deleting:\n")
d.pop('c')
for key, value in d.items():
    print(key, value)

print("\nAfter re-inserting:\n")
d['c'] = 3
for key, value in d.items():
    print(key, value)

d.update({'e': 5})
print(d)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
    print(key, value)

print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
    print(key, value)

od.update({'e': 5})
print(od)
