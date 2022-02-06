class Queue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError
        return self.items[index]

# requisito feito com https://www.geeksforgeeks.org/stack-in-python/ 
