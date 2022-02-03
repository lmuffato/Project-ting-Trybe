class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head_value = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def insert_first(self, value):
        first_value = Node(value)
        first_value.next = self.head_value
        self.head_value = first_value
        self.__length += 1

    def enqueue(self, value):
        last_value = Node(value)
        current_value = self.head_value

        if current_value is None:
            return self.insert_first(value)

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
        return value_to_be_removed.value

    def search(self, index):
        value_returned = None
        value_to_be_returned = self.head_value

        if 0 > index or index > self.__length or self.__length == 0:
            raise IndexError

        if value_to_be_returned:
            while index > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                index -= 1

            if value_to_be_returned:
                value_returned = Node(value_to_be_returned.value)
        return value_returned.value
