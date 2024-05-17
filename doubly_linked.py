class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next:
                current = current.next
            current.prev.next = None

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

# Example usage
linked_list = DoublyLinkedList()
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_end(30)
linked_list.display_forward()  # Output: 20 10 30
linked_list.delete_at_beginning()
linked_list.display_forward()  # Output: 10 30
linked_list.delete_at_end()
linked_list.display_forward()  # Output: 10
linked_list.display_backward() # Output: 10
