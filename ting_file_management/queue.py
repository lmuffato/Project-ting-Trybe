class Queue:
    def __init__(self):
        self.files = list()

    def __len__(self):
        return len(self.files)

    def enqueue(self, value):
        self.files.append(value)

    def dequeue(self):
        return self.files.pop(0)

    def search(self, index):
        if index < 0 or index > self.__len__():
            raise IndexError

        return self.files[index]
