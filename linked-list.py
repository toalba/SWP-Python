# this script will explain the linked list data structure
# Start 8:44

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class Linked_list:
    def __init__(self):
        self.head = None

    # Inserting a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

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

#End 8:46

if __name__ == "__main__":
    print("Linked List")
    linked_list = Linked_list()
    linked_list.insert_at_beginning(1)
