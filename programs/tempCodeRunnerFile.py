class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, prev_node_data, data):
        if self.is_empty():
            print("Cannot perform insertion. The list is empty.")
            return

        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node = Node(data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

        print("Cannot perform insertion. Previous node not found.")

    def delete(self, data):
        if self.is_empty():
            print("Cannot perform deletion. The list is empty.")
            return

        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

        print("Cannot perform deletion. Node not found.")

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display_forward(self):
        if self.is_empty():
            print("The list is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        if self.is_empty():
            print("The list is empty.")
            return

        current = self.head
        while current.next:
            current = current.next

        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Example usage with user input:
my_list = DoublyLinkedList()

while True:
    print("1. Append")
    print("2. Prepend")
    print("3. Insert After")
    print("4. Delete")
    print("5. Search")
    print("6. Display Forward")
    print("7. Display Backward")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the value to append: "))
        my_list.append(data)
    elif choice == 2:
        data = int(input("Enter the value to prepend: "))
        my_list.prepend(data)
    elif choice == 3:
        prev_data = int(input("Enter the value of the previous node: "))
        data = int(input("Enter the value to insert: "))
        my_list.insert_after(prev_data, data)
    elif choice == 4:
        data = int(input("Enter the value to delete: "))
        my_list.delete(data)
    elif choice == 5:
        data = int(input("Enter the value to search: "))
        if my_list.search(data):
            print("Value found.")
        else:
            print("Value not found.")
    elif choice == 6:
        my_list.display_forward()
    elif choice == 7:
        my_list.display_backward()
    elif choice == 8:
        break
    else:
        print("Invalid choice. Try again.\n")
