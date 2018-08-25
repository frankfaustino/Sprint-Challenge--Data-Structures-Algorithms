from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def enqueue(self, item):
        self.size += 1
        self.storage.append(item)
  
    def dequeue(self):

        node = self.storage.pop(-1)
        if node:
            self.size -= 1
            return node

    def len(self):
        return self.size

