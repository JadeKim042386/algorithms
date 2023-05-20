class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return f"Node({self.data})"

class LinkedQueue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
    
    def __iter__(self):
        node = self.front
        while node:
            yield node.data
            node = node.next
        
    def __repr__(self) -> str:
        return "<-".join([str(item) for item in self])
    
    def __len__(self):
        return len(tuple(iter(self)))
    
    def is_empty(self):
        return len(self) == 0
    
    def put(self, data):
        node = Node(data)
        if self.is_empty():
            self.front = self.rear = node
        else:
            assert isinstance(self.rear, Node)
            self.rear.next = node
            self.rear = node

    def get(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        assert isinstance(self.front, Node)
        node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return node.data

    def clear(self):
        self.front = self.rear = None