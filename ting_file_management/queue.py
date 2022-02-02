from typing import Union


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Union[Node, None] = None

    def __str__(self):
        return f'Node(value={self.value}, next={self.next})'


class Queue:
    def __init__(self):
        self.__length = 0
        self.front: Union[Node, None] = None
        self.rear: Union[Node, None] = None

    def __len__(self):
        return self.__length

    def __str__(self):
        node = self.front
        if node is not None:
            return node.__str__()
        else:
            return 'Queue is empty'

    def enqueue(self, value):
        new_node = Node(value)
        previous_last_node = self.rear
        self.__length += 1
        if previous_last_node is None:
            self.front = new_node  # first node is both front and rear
            self.rear = new_node
            return None
        previous_last_node.next = new_node
        self.rear = new_node  # updates end of the link

    def dequeue(self):
        removed_node = self.front
        if removed_node is None:
            self.__length = 0
            self.rear = None
            return None
        if removed_node is not None:
            self.front = removed_node.next
            removed_node.next = None
            self.__length -= 1
        return removed_node.value  # Return the node so it can be used

    def __get_node(self, node: Node, index):
        if index == 0:
            return node.value
        return self.__get_node(node.next, index - 1)

    def search(self, index):
        if self.__length <= index or index < 0:
            raise IndexError('Index out of bounds')
        return self.__get_node(self.front, index)
