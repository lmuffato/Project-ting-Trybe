class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return not bool(self.__len__())

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index):
        if index >= 0 and self._data[index]:
            return self._data[index]
        raise IndexError
