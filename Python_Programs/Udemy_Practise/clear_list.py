lst1 = [9, 2, 34, 2, 5, 9, 16]
print(f"List1: {lst1}")
lst1.clear()
print(f"List1 after clearing: {lst1}")
lst2 = [19, 'eh', 16]
print(f"List2: {lst2}")
del lst2[:1]
print(f"List2 after deleting first 2 elements: {lst2}")
del lst2[:]
print(f"List2 after deleting all elements: {lst2}")


