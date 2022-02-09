class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.__len__() == 0:
            return None

        dequeued_value = self._data[0]
        self._data = self._data[1:]
        return dequeued_value

    def search(self, index):
        if index < 0 or self.__len__() < index + 1:
            raise IndexError

        return self._data[index]
