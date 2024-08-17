# Write a Python program to create a class representing a linked list data sctructure
# Include methods for displaying linked list data, inserting and deleting nodes.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if node.next is None:
            node.next = Node(data)
        else:
            self._insert(data, node.next)

    def display(self):
        self._display(self.root)

    def _display(self, node):
        if node is not None:
            print(node.data, end=" ")
            if node.next is not None:
                print("", end="-> ")
            self._display(node.next)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return None
        if node.data == data:
            return node.next
        node.next = self._delete(node.next, data)
        return node


list1 = LinkedList()
list1.insert(4)
list1.insert(6)
list1.insert(2)
list1.insert(8)

list1.delete(2)

list1.display()
