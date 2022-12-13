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

    def delete(self, key):
        temp = self.head

        # if key is head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            print("Not part of Linked List")
            return

        # unlink the node
        prev.next = temp.next
        prev = None


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(6)

llist.printList()

print("Delete Node:")
llist.delete(1)
print("Print List")
llist.printList()

print("Delete Node:")
llist.delete(6)
print("Print List")
llist.printList()


print("Delete Node:")
llist.delete(3)
print("Print List")
llist.printList()