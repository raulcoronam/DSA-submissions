class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None 
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = Node(-1)
        self.right = Node (-1)
        self.left.next = self.right
        self.right.prev = self.left   

    def isEmpty(self) -> bool:
        return self.left.next == self.right 

    def append(self, value: int) -> None:
        newNode = Node(value)
        last_node = self.right.prev

        last_node.next = newNode
        newNode.prev = last_node 
        newNode.next = self.right
        self.right.prev = newNode 

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        first_node = self.left.next 

        first_node.prev = newNode
        newNode.next = first_node
        self.left.next = newNode
        newNode.prev = self.left 

    def pop(self) -> int:
        if self.left.next == self.right: 
            return -1
        else: 
            last_node = self.right.prev
            new_last_node = last_node.prev
            new_last_node.next = self.right
            self.right.prev = new_last_node
            return last_node.value

    def popleft(self) -> int:
        if self.left.next == self.right: 
            return -1
        else: 
            first_node = self.left.next 
            new_first_node = first_node.next 

            new_first_node.prev = self.left
            self.left.next = new_first_node 
            return first_node.value

        
