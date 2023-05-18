class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"Node({self.data})"
    
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next
    
    def __repr__(self) -> str:
        return "->".join(str(item) for item in self)
    
    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range")
        for i, node in enumerate(self):
            if i == index:
                return node
        return None
    
    def __setitem__(self, index, data):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            for _ in range(len(self) - 1):
                temp = temp.next
            temp.next = new_node

    def insert_nth(self, index, data):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
    
    def delete_nth(self, index):
        if not 0 <= index < len(self) - 1:
            raise ValueError("list index out of range")
        delete_node = self.head
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
        return delete_node.data
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def print_list(self):
        print(self)