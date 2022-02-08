class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        str_items = ""
        for i in range(self.__len__()):
            value = self._data[i]
            str_items += str(value)
            if i + 1 < self.__len__():
                str_items += ", "

        return "Queue(" + str_items + ")"

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index):
        if 0 <= index < self.__len__():
            return self._data[index]

        raise IndexError
