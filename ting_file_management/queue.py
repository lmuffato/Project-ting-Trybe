from ting_file_management.util import get_files_name

class Queue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        current_out = self.queue[0]
        self.queue.pop(0)
        return current_out

    def search(self, index):
        # por que o method self.__len__ não funciona nesse caso?
        if index >= len(self.queue) or index < 0:
            raise IndexError
        return self.queue[index]

queue = Queue()
queue.enqueue(12)
queue.enqueue("oi")
queue.enqueue("hey")
get_files_name(queue)
