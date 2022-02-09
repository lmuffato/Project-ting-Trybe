class Queue:
    def __init__(self):
        self.list = list()

    def __len__(self):
        return len(self.list)

    def enqueue(self, value):
        return self.list.append(value)

    def dequeue(self):
        return self.list.pop(0)

    def search(self, index):
        if(index < 0 or index > len(self.list)):
            raise IndexError
        return self.list[index]
