arr1 = [1, 2, 4, -9, 11, 0,  18, 3, 1]
print(f"Maximum of array1: {max(arr1)}")
arr2 = [1, 6, 0, 3, -4, 5, 67, 66, 3, -3, 9, 2, 65, -67]
m = arr2[0]
for i in range(1, len(arr2)):
    if arr2[i] > m:
        m = arr2[i]
print(f"Maximum of array2: {m}")






