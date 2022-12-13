# To check whether the array is Monotonic or not.
# An array is monotonic if it is either monotone increasing or monotone decreasing.

# arr = [1, 1, 5, 25, 35, 54, 43]
arr = list(map(int, input("Enter array to check for Monotonic:").split()))
print(f"Array: {arr}")
ln = len(arr)
if all(arr[i-1] <= arr[i] for i in range(1, ln)):
    print("Monotone increasing")
elif all(arr[i - 1] >= arr[i] for i in range(1, ln)):
    print("Monotone decreasing")
else:
    print("Not Monotonic")
