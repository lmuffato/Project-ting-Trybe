class Queue:
    def __init__(self):
        self._list = list()

    def __len__(self):
        return len(self._list)

    def enqueue(self, value):
        self._list.append(value)

    def dequeue(self):
        removed_item = self._list[0]
        self._list.pop(0)
        return removed_item

    def search(self, index):
        """Aqui irá sua implementação"""
