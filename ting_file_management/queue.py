class Queue:
    def __init__(self):
        self.list_ting = list()

    def __len__(self):
        return len(self.list_ting)

    def enqueue(self, value):
        self.list_ting.append(value)

    def dequeue(self):
        return self.list_ting.pop(0)

    def search(self, index):
        if self.__len__() > index >= 0:
            return self.list_ting[index]
        else:
            raise IndexError
