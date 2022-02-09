from __init__ import Node


class Queue:
    def __init__(self):
        self.head_value = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        first_value = Node(value)
        first_value.next = self.head_value
        self.head_value = first_value
        self.__length += 1

    def dequeue(self):
        value_to_be_removed = self.head_value
        if value_to_be_removed:
            self.head_value = self.head_value.next
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed

    def search(self, index):
        """Aqui irá sua implementação"""

joao = Queue()
joao.enqueue(2)
print(joao)
# print(Queue.enqueue(3))
# Queue = ([1,2,3,4,5,6,7,8])
# print(Queue)
