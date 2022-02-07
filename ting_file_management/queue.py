class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.queue = list()


    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        # return self.queue[index] if 0 <= index <= self.__len__() -1 else raise IndexError 'ternário' n funfa com o raise
        if 0 <= index <= self.__len__() - 1:
            return self.queue[index]
        else:
            raise IndexError
