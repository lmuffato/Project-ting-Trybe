class Queue:
    def __init__(self):
        self.list = []
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        self.list.append(value)
        self.__length += 1

    def dequeue(self):
        value = self.list.pop(0)
        self.__length -= 1
        return value

    def search(self, index):
        if index < 0 or index > (self.__length - 1):
            raise IndexError
        return self.list[index]
