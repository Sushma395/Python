# Python program to demonstrate
# userlist

# UserList is a list-like container that acts as a wrapper around the list objects.
# This is useful when someone wants to create their own list with some modified or additional functionality.


from collections import UserList


# Creating a List where
# deletion is not allowed
class MyList(UserList):

    # Function to stop deletion
    # from List
    def remove(self, s=None):
        raise RuntimeError("Remove not allowed")

    # Function to stop pop from
    # List
    def pop(self, s=None):
        raise RuntimeError("Pop not allowed")

    # Function to stop copy from
    # List
    def __del__(self):
        raise RuntimeError("Deletion not allowed")


# Driver's code
L = MyList([1, 2, 3, 4])

print("Original List")
print(L)

# Extend List
L.extend([1, 2])

print("After extending the list")
print(L)

# Inserting to List"
L.append(5)
print("After Insertion")
print(L)

# Deleting From List
L.remove()
L.pop()
print(L)

del L
