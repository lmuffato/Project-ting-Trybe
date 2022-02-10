class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue():
    def __init__(self):
        self.fila = []

    def __len__(self):
        return len(self.fila)

    def enqueue(self, value):
        return self.fila.append(value)

    def dequeue(self):
        return self.fila.pop(0)

    def search(self, index):
        pass
    
    def show_queue(self):
        aux = self.head_value
        while aux is not None:
            print(f' {aux.value} -->',end='')
            aux = aux.next
        print(None)
    
    def __str__(self):
        aux = self.head_value
        retorno = '' 
        while aux is not None:
            retorno += f' {aux.value} -->'
            aux = aux.next
        return (retorno + '\n')
    
    def is_empty(self):
        return not self.__length
    
pessoa = (Node('Fernanda'))
pessoa.next = 'ivan'
print(pessoa.value)
# joao = Queue()
# # print(joao.tail_value)
# joao.enqueue(2)
# joao.enqueue(3)
# joao.enqueue(4)
# joao.show_queue()
# joao.show_queue()
# print(Queue.enqueue(3))
# Queue = ([1,2,3,4,5,6,7,8])
# print(Queue)
