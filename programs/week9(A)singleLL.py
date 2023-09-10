class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_begin(self, new_node):  # Passing the new_node directly
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def add_end(self, new_node):  # Passing the new_node directly
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            
# ...

    def add_specific(self, new_node, pos):  # Passing the new_node directly
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            for i in range(1, pos):
                p = current
                current = current.next
            p.next = new_node
            new_node.next = current
            
    def display(self):
        current = self.head
        while current:
            print(current.data, end='  ')
            current = current.next
        print()
        
    def delete_beg(self):
        current = self.head
        self.head = current.next
        del current

    def delete_end(self):
        current = self.head
        while current.next is not None:
            p = current
            current = current.next
        p.next = None
        del current

    def del_specific(self, pos):
        current = self.head
        for i in range(1, pos-1):
            current = current.next
        p = current.next
        current.next = p.next
        del p

LL1 = LinkedList()
print("1. INSERT AT BEGINNING")
print("2. INSERT AT THE END")
print("3. INSERT AT SPECIFIC POSITION")
print("4. DISPLAY")
print("5. DELETE FROM BEGINNING")
print("6. DELETE FROM ENDING")
print("7. DELETE FROM SPECIFIC POSITION")
print("8. EXIT")

while True:
    op = int(input("Enter your choice: "))
    
    if op == 1:
        data = int(input("Enter the element: "))
        new_node = Node(data)
        LL1.add_begin(new_node)
    elif op == 2:
        data = int(input("Enter the element: "))
        new_node = Node(data)
        LL1.add_end(new_node)
    elif op == 3:
        pos = int(input("Enter the position: "))
        data = int(input("Enter the element: "))
        new_node = Node(data)
        LL1.add_specific(new_node, pos)
    elif op == 4:
        print("The list:", end='  ')
        LL1.display()
    elif op == 5:
        LL1.delete_beg()
    elif op == 6:
        LL1.delete_end()
    elif op == 7:
        pos = int(input("Enter the position: "))
        LL1.del_specific(pos)
    elif op == 8:
        exit()