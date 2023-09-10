class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.size=5
    def push(self,e):
        if self.top==self.size-1:
            print("Stack Overflow")
        else:
            self.top+=1
            self.stack.append(e)
    def pop(self):
        if self.top==-1:
            print("Stack Underflow")
        else:
            print("Element to be deleted:",self.stack.pop(self.top))
            self.top-=1
    def display(self):
        if self.top==-1:
            print("No elements to be dislayed")
        else:
            print(self.stack[self.top],"-->top")
            for i in range (self.top-1,-1,-1):
                print(self.stack[i])
stackobj=Stack()
while True:
    print("\n-----*STACK MENU*-----\n1.push\n2.pop\n3.display\n4.exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        e=int(input("Enter element to be inserted:"))
        stackobj.push(e)
    elif ch==2:
        stackobj.pop()
    elif ch==3:
        stackobj.display()
    elif ch==4:
        break
    else:
        print("Invalid choice")
            
            
            
            
            
            
            
            