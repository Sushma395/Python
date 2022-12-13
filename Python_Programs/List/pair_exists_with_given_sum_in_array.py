# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

def search(arr, x):
    l = 0
    r = len(arr)-1
    arr.sort()
    print(f"sorted array: {arr}")
    output = []
    while l < r:
        if arr[l] + arr[r] == x:
            output.append([arr[l], arr[r]])
            l += 1
            r += 1
        elif arr[r] + arr[l] > x:
            r -= 1
        else:
            l += 1
    return output


arr = [1, -3, 7, 9, 3, -4, 11, -2, 15, 8]
print(f"given array: {arr}")
x = 9
print(f"x : {x}")
print(f"pair with sum equal to x: {search(arr, x)}")
