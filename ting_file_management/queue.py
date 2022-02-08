class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index >= len(self._data):
            raise IndexError

        for i in range(len(self._data)):
            if self._data[i] == self._data[index]:
                return self._data[i]
