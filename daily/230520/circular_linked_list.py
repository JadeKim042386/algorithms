class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return f"Node({self.data})"

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while True:
            yield node.data
            node = node.next
            if node == self.head:
                break
    
    def __len__(self):
        return len(tuple(iter(self)))
    
    def __repr__(self) -> str:
        return "->".join([str(item) for item in self])
    
    def insert_nth(self, index, data):
        if not 0 <= index < len(self):
            raise IndexError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = self.tail.next = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            if index == len(self) - 1:
                self.tail = new_node
    
    def insert_head(self, data):
        self.insert_nth(0, data)

    def insert_tail(self, data):
        self.insert_nth(len(self), data)
    
    def delete_nth(self, index):
        if not 0 <= index < len(self):
            raise IndexError("list index out of range")
        delete_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        elif index == 0:
            self.tail.next = self.tail.next.next
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
            if index == len(self) - 1:
                self.tail = temp
        return delete_node.data

    def delete_head(self):
        self.delete_nth(0)
    
    def delete_tail(self):
        self.delete_nth(len(self) - 1)
    
    def is_empty(self):
        return len(self) == 0

