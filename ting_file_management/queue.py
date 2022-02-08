class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if not bool(self.__len__()):
            return None

        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        """Aqui irá sua implementação"""
