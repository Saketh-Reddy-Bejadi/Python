class Stack:
    def __init__(se):
        se.stack=[]
        se.size=5
        se.top=-1
    def push(se,e):
        if se.top==se.size-1:
            print("Stack Overflow")
        else:
            se.top+=1
            se.stack.append(e)
    def pop(se):
        if se.top==-1:
            print("Stack Underflow")
        else:
            print(f"element to be deleted:{se.stack.pop()}")
            se.top-=1
    def display(se):
        if se.top==-1:
            print("Stack is empty")
        else:
            print(se.stack[se.top],"<--top")
            for i in range (se.top-1,-1,-1):
                print(se.stack[i])
st=Stack()
while True:
        print("---*--Stack Menu--*---\n1.push\n2.pop\n3.display\n4.exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            e=input("Enter element to be inserted:")
            st.push(e)
        elif ch==2:
            st.pop()
        elif ch==3:
            st.display()
        elif ch==4:
            break
        else:
            print("Invalid Choice")
    
        