class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui."""
        self.values = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.values)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        return self.values.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.values.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index > len(self.values):
            raise IndexError
        return self.values[index]
