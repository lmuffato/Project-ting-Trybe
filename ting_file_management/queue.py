# https://pythonhelp.wordpress.com/2012/09/25/filas-e-pilhas-em-python/


class Queue:
    # Requisito 1
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.data = []

    def __len__(self):
        """Aqui irá sua implementação"""
        self.__length = len(self.data)
        return self.__length

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.data.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0:
            raise IndexError
        else:
            return self.data[index]
