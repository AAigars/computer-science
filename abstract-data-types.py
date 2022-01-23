class Queue:
    """
    Simple implementation of a Queue (First in First Out) using a dynamic data structure (List)
    """
    def __init__(self, size = -1):
        self.list = []
        self.size = size

    def enQueue(self, data):
        if(not self.isFull()):
            self.list.append(data)

    def deQueue(self):
        if(not self.isEmpty()):
            return self.list.pop(0)

    def isEmpty(self):
        return len(self.list) == 0

    def isFull(self):
        return False if self.size == -1 else len(self.list) == self.size 