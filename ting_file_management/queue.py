class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.list = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.list)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        return self.list.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.list.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index > (self.__len__() - 1):
            raise IndexError
        return self.list[index]
