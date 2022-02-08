class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self._data:
            return self._data.pop(0)
        return None

    def search(self, index):
        try:
            return self._data[index]
        except IndexError:
            raise IndexError

""" queue = Queue()
print(queue.search(1)) """

