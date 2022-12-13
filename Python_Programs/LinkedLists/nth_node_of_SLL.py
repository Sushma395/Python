
# Write a function to get Nth node in a Linked List

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def NthNode(self, n):
        temp = self.head
        count = 0

        # Loop while end of linked list is not reached
        while temp:
            if count == n:
                return temp.data
            count += 1
            temp = temp.next

        # if we get to this line, the caller was asking
        # for a non-existent element so we assert fail
        assert(False)


llist = LinkedList()
llist.push(11)
llist.push(12)
llist.push(13)
llist.push(14)
llist.push(15)

n = 2
print(f"{n}th node is: {llist.NthNode(n)}")