class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        value = self.data[0]
        del self.data[0]
        return value

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index >= len(self.data):
            raise IndexError 
        value = self.data[index]
        return value
    
