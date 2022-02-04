class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        queue_list_item = self._data[0]
        del self._data[0]

        return queue_list_item

    def search(self, index):
        """Aqui irá sua implementação"""
