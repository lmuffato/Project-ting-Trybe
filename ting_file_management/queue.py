class Queue:
    # a funcao init eh usada para criar a varievel que sera populada pela fila
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.storage_row = []

    # a funcao len retorna o tamanho da fila
    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.storage_row)

    # a funcao enqueue adiciona um elemento no final da fila com o append
    def enqueue(self, value):
        """Aqui irá sua implementação"""
        return self.storage_row.append(value)

    # a funcao dequeue retira o primeiro elemento da fila com o pop(0)
    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.storage_row.pop(0)

    # a funcao search busca o dict pelo index dentro da fila
    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0:
            raise IndexError()
        return self.storage_row[index]
