class Stack:
    def __init__(self):
        self.stack=[]
        self.size=5
        self.top=-1
    def insert(self,x):
        if self.top==self.size-1:
            print("Stack is Overflow")
        else:
            print(f"Element Inserted: {x}")
            self.top+=1
            self.stack.append(x)
    def delete(self):
        if self.top==-1:
            print("Stack is Underflow")
        else:
            print(f"Element to be deleted:{self.top}")
            self.stack.pop(self.top)
            self.top-=1
    def display(self):
        if self.top==-1:
            print("No element to be display")
        else:
            print(f"{self.stack[self.top]} <--top")
            for i in range (self.top-1,-1,-1):
                print(self.stack[i])
obj=Stack()
while True:
    print("-----*-----*-----\nStack Menu")
    print("1.Insert\n2.Delete\n3.Display\n4.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        x=int(input("Enter element to be inserted:"))
        obj.insert(x)
    elif ch==2:
        obj.delete()
    elif ch==3:
        obj.display()
    elif ch==4:
        break
    else:
        print("Invalid choice")