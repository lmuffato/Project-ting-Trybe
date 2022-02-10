class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.head = None
        self._size = 0

    def __len__(self):
        """Aqui irá sua implementação"""
        return self._size

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(value)
        else:
            self.head = Node(value)
        self._size = self._size + 1

    def dequeue(self):
        """Aqui irá sua implementação"""
        pointer = self.head
        if pointer:
            self.head = self.head.next
            pointer.next = None
            self._size = self._size - 1
        return pointer.data

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index > self._size - 1:
            raise IndexError
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError
        if pointer:
            return pointer.data
        else:
            raise IndexError
