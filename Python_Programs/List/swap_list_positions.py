# Python3 program to swap elements
# at given positions
def swap_positions(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    print(f"Array after swapping first, last elements is: {arr}")


arr = [1, 1, 5, 25, 35, 54, 43, 'am']
print(f"List is: {arr}")
a, b = map(int, input("Enter positions to be swapped in list: ").split(" "))
swap_positions(arr, a-1, b-1)