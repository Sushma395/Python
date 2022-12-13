# Left Rotate will shift all elements to left by one index and place the first index element to the last index.
# Right Rotate will shift all elements to right by one index and place the last index element to the first index.

def left_rotate(arr1, a, ln):
    # code for left rotation by 'a' positions
    arr2 = []
    for i in range(0, ln - a):
        arr2.append(arr1[i + a])
    for i in range(0, a):
        arr2.append(arr1[i])
    print(arr2)


def right_rotate(arr1, a, ln):
    # code for right rotation by 'a' positions method 2
    arr2 = arr1[ln-a:] + arr1[:ln-a]
    print(arr2)


arr1 = [1, 2, 4, -9, 11, 0, 18, 3, 5, 1]
print(f"Array: {arr1}")
ln = len(arr1)
a = int(input("Number of positions to be rotated: "))
b = 0
while b != 1 and b != 2:
    b = int(input("Enter 1 for left rotation or 2 for right rotation:"))
    print(b)
else:
    if b == 1:
        left_rotate(arr1, a, ln)
    if b == 2:
        right_rotate(arr1, a, ln)
