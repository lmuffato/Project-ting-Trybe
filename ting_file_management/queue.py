class Queue:
    # GO!
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def get(self):
        return self._data

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        try:
            value = self._data[0]
            self._data.pop(0)
            return value
        except IndexError:
            raise IndexError

    def search(self, index):
        if index < 0:
            raise IndexError
        try:
            value = self._data[index]
            return value
        except IndexError:
            raise IndexError
