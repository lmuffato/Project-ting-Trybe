from pyparsing import empty


class Queue:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        if len(self.data) == 0:
            return self.data.append(value)
        else:
            auxiliary_list = list()
            auxiliary_list.append(value)
            self.data = self.data + auxiliary_list

    def dequeue(self):
        if self.data is empty():
            return None
        value = self.data[0]
        del self.data[0]
        return value

    def search(self, index):
        if index < 0 or len(self.data) == 0:
            raise IndexError
        return self.data[index]
