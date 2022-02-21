class Queue:
    # CONSTRUTOR
    def __init__(self):
        # list() -> usar estruturta de lista para guardar
        # as informações da pilha
        self.list = list()

    # RETORNA O COMPRIMENTO DA LISTA
    def __len__(self):
        # método para verifica o comprimento da lista
        return len(self.list)

    # ADICIONAR DADOS
    def enqueue(self, value):
        # adiciona o dado no topo da lista
        return self.list.append(value)

    # REMOVER DADOSS
    def dequeue(self):
        # remove o dado no topo da lista
        return self.list.pop(0)

    # BUSCAR DADO
    def search(self, index):
        # Se o index for menor que 0 ou maior que a lista
        if(index < 0 or index > len(self.list)):
            # retorna a exception erro indexError
            raise IndexError
        return self.list[index]


# teste automatizado
# python3 -m pytest tests/test_queue.py
