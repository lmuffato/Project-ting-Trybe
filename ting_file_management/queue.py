class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue():
    def __init__(self):
        self.head_value = None
        self.tail_value = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        if self.is_empty():
            first_value = Node(value)
            first_value.next = self.head_value
            self.__length += 1
            self.head_value = first_value
            return

        last_value = Node(value)
        current_value = self.head_value

        while current_value.next:
            current_value = current_value.next
        current_value.next = last_value
        self.__length += 1

    def dequeue(self):
        value_to_be_removed = self.head_value
        if value_to_be_removed:
            self.head_value = self.head_value.next
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed

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
