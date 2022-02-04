from structures.node import Node


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def insert_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.__length += 1

    def insert_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.__length += 1

    def insert_at(self, value, position):
        if position < 1:
            return self.insert_first(value)
        if position >= len(self):
            return self.insert_last(value)
        left_value = self.head
        while position > 1:
            left_value = left_value.next
            position -= 1
        new_node = Node(value)
        new_node.next = left_value.next
        left_value.next.previous = new_node
        left_value.next = new_node
        new_node.previous = left_value
        self.__length += 1

    def remove_first(self):
        value_to_be_removed = self.head
        if value_to_be_removed:
            self.head = self.head.next
            self.head.previous = None
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed

    def remove_last(self):
        if len(self) <= 1:
            return self.remove_first()
        value_to_be_removed = self.tail
        if value_to_be_removed:
            self.tail = self.tail.previous
            self.tail.next = None
            value_to_be_removed.previous = None
            self.__length -= 1
        return value_to_be_removed

    def remove_at(self, position):
        if position < 1:
            return self.remove_first()
        if position >= len(self):
            return self.remove_last()

        previous_to_be_removed = self.head

        while position > 1:
            previous_to_be_removed = previous_to_be_removed.next
            position -= 1

        value_to_be_removed = previous_to_be_removed.next
        previous_to_be_removed.next = value_to_be_removed.next
        value_to_be_removed.next.previous = previous_to_be_removed
        value_to_be_removed.next = None
        value_to_be_removed.previous = None
        self.__length -= 1

        return value_to_be_removed

    def get_element_at(self, position):
        if position < 0:
            raise IndexError
        value_returned = None
        value_to_be_returned = self.head
        if value_to_be_returned:
            while position > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                position -= 1
            if value_to_be_returned and position == 0:
                value_returned = Node(value_to_be_returned.value)
            else:
                raise IndexError
        return value_returned

    def get_last(self):
        return self.tail

    def is_empty(self):
        return not self.__length


# Para testar, apenas rode o arquivo com: `python3 linked_list_content.py` :)
# if __name__ == "__main__":
#     linked_list = LinkedList()

#     print(linked_list.is_empty()) # saída: True
#     linked_list.insert_first(1)
#     print(linked_list)

#     linked_list.insert_first(2)
#     print(linked_list)
#     linked_list.insert_last(3)
#     print(linked_list)

#     linked_list.remove_last()
#     print(linked_list)

#     linked_list.remove_first()
#     print(linked_list)

#     linked_list.insert_at(5, 1)
#     print(linked_list)

#     linked_list.remove_at(0)
#     print(linked_list)

#     linked_list.insert_at(6, 1)
#     linked_list.insert_at(7, 2)
#     linked_list.insert_at(8, 3)
#     linked_list.insert_at(9, 4)
#     print(linked_list.get_element_at(3))
