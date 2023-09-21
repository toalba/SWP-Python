# bidirectional linked list implementation
# Start 8:58

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Linked List class
class Linked_list:
    def __init__(self):
        self.head = None
    
    # Inserting a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        new_node.prev = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            new_node.next = None

