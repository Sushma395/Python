# arr = [1, 1, 5, 25, 35, 54, 43, 'am']
arr = list(input("Enter array to swap first, last elements:").split())
print(f"Array is: {arr}")
ln = len(arr)
arr[ln-1], arr[0] = arr[0], arr[ln-1]
print(f"Array after swapping first, last elements is: {arr}")
