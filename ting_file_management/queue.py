class Queue:
    def __init__(self):
        self.data = list()
    # guarda tudo

    def __len__(self):
        return len(self.data)
    # returna o tamanho

    def enqueue(self, value):
        return self.data.append(value)
    # adiciona na ultima possição

    def dequeue(self):
        return self.data.pop(0)
    # tira o primeiro da fila pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError
        return self.data[index]
    # pesquisa pelo index
