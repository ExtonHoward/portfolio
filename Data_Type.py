

class Stack:
    #LIFO data structure
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push (self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    def size(self):
        return len(self.items)

class Queue:
    #FIFO data structure
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue (self):
        self.items.pop()
    def size(self):
        return len(self.items)

class Node:
    #creates nodes for a linked list
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def print_node(self):
        print (self.data)

class LinkedList:
    #head holds the node at the head of your linked list. First time you create a linked list with this code, the result is a new, empty linked list. After that, it holds the head node.
    def __init__(self):
        self.head = None
    def append_node(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    def print_list(self):
        node = self.head
        while node is not None:
            print (node.data)
            node = node.next

    def search(self, target):
        current = self.head
        while current != None:
            if current.data == target:
                print ("Found it")
                return True
            else:
                current = current.next
        print ("Not found")
        return False

