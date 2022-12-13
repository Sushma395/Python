# Siemens round 2
# find max prefix common for all
lst = ["Plane", "Plate", "Please", "plus" ]
base = list(lst[0])
print(base)
common = []
for i in range(0, len(base)):
    for j in range(1, len(lst)):
        if i <= j:
            if base[i] == lst[j][i]:
                if lst[j][i] not in common:
                    common.append(lst[j][i])

print(common)





