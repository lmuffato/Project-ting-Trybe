# Ref: https://github.dev/tryber/sd-10a-live-lectures/tree/Aula37.2

class Queue:
    def __init__(self):
        # """Inicialize sua estrutura aqui"""
        self._data = list()

    def __len__(self):
        # """Aqui irá sua implementação"""
        return len(self._data)

    def is_empty(self):         # indica se a pilha esta vazia ou não
        return not bool(self.__len__)

    def enqueue(self, value):
        # """Aqui irá sua implementação"""
        self._data.append(value)

    def dequeue(self):
        # """Aqui irá sua implementação"""
        if self.is_empty():
            return None

        # O primeiro elemento é o que está a mais tempo na fila: FIFO
        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        # """Aqui irá sua implementação"""
        if self.is_empty():
            return None

        if index < 0:
            raise IndexError

        value = self._data[index]
        return value
