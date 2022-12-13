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

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            current = current.next
            current.next = prev
            prev = current




llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(51)
llist.push(61)

print(f"length of linked list is: {llist.reverse()}")
llist.printList()