# Python3 program to find length of list without len()
def length(lst):
    # len(lst) can be used instead
    count = 0
    for _ in lst:
        count += 1
    print(f"Length of list is: {count}")


lst = [1, 1, 5, 25, 35, 54, 43, 'am']
print(f"List is: {lst}")
length(lst)
