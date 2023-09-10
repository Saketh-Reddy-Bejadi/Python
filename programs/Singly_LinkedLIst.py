class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    head = None
    
    def insert_at_beginning(self):
        data = int(input('Enter data: '))
        new_node = Node(data)
        new_node.next = SLL.head
        SLL.head = new_node
        
    def insert_at_end(self):
        data = int(input('Enter data: '))
        new_node = Node(data)
        
        if SLL.head is None:
            SLL.head = new_node
        else:
            temp = SLL.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            
    def insert_at_location(self):
        data = int(input('Enter data: '))
        new_node = Node(data)
        
        if SLL.head is None:
            SLL.head = new_node
        else:
            loc = int(input('Enter the element after which you want to insert: '))
            temp = SLL.head
            while temp.data != loc:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            
    def delete_at_beginning(self):
        if SLL.head is None:
            print('No element to delete')
        else:
            deleted_item = SLL.head.data
            SLL.head = SLL.head.next
            print('The deleted item:', deleted_item)
            
    def delete_at_location(self):
        if SLL.head is None:
            print('No element to delete')
        else:
            data = int(input('Enter the element to be deleted: '))
            temp = SLL.head
            prev = None
            while temp is not None and temp.data != data:
                prev = temp
                temp = temp.next
            if temp is None:
                print('Element not found')
            else:
                prev.next = temp.next
                
    def delete_at_end(self):
        if SLL.head is None:
            print('No element to delete')
        else:
            temp = SLL.head
            prev = None
            while temp.next is not None:
                prev = temp
                temp = temp.next
            if prev is None:
                SLL.head = None
            else:
                prev.next = None
            
    def display(self):
        temp = SLL.head
        while temp is not None:
            print(temp.data, end=' --> ')
            temp = temp.next
            
ob = SLL()

while True:
    print("\n1 to insert at the beginning")
    print("2 to insert at the end")
    print("3 to insert at a specific location")
    print("4 to delete at the beginning")
    print("5 to display")
    print("6 to delete at a specific location")
    print("7 to delete at the end")
    print("8 to exit")
    
    choice = int(input("What do you want to do? "))
    
    if choice == 1:
        ob.insert_at_beginning()
    elif choice == 2:
        ob.insert_at_end()
    elif choice == 3:
        ob.insert_at_location()
    elif choice == 4:
        ob.delete_at_beginning()
    elif choice == 5:
        ob.display()
    elif choice == 6:
        ob.delete_at_location()
    elif choice == 7:
        ob.delete_at_end()
    elif choice == 8:
        break
    else:
        print('Invalid option')
