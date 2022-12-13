#descending without method
lst = [6, 8, 3, 0, -3, 11]
lst2 = []
for i in range(0,len(lst)):
    lst2.append(max(lst))
    lst.remove(max(lst))
print(lst2)