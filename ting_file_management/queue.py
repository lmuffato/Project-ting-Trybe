class Queue:
    def __init__(self):
        self.list_ting = list()
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        self.list_ting.append(value)
        self.__length += 1

    def dequeue(self):
        self.__length -= 1
        return self.list_ting.pop(0)

    def search(self, index):
        if self.__len__() > index >= 0:
            return self.list_ting[index]
        else:
            raise IndexError
