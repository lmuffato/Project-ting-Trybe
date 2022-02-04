class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return (f"Node(value={self.value},"
                f"next={self.next},"
                f"previous={self.previous})")
