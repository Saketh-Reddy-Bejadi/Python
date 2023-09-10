class DLL:
    head=None
    def __init__(self):
        self.data=None
        self.next=None
        self.prev=None
    def insertatbeg(self):
        newnode=DLL()
        newnode.data=int(input('enter data:'))
        newnode.next=None
        newnode.prev=None
        if DLL.head==None:
            DLL.head=newnode
        else:
            newnode.next=DLL.head
            DLL.head.prev=newnode
            DLL.head=newnode
    def insertatloc(self):
        newnode=DLL()
        newnode.data=int(input('enter data:'))
        newnode.next=None
        newnode.prev=None
        
        if DLL.head==None:
            DLL.head=newnode
        else:
            x=int(input('enter the ele afte which uh wana insert ele:'))
            temp=DLL.head
            while temp.data!=x:
                temp=temp.next
            newnode.prev=temp
            newnode.next=temp.next
            temp.next=newnode
    def insertatend(self):
        newnode=DLL()
        newnode.data=int(input('enter data:'))
        newnode.next=None
        newnode.prev=None
        if DLL.head==None:
            DLL.head=newnode
        else:
            temp=DLL.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp
    def deleteatbeg(self):
        if DLL.head==None:
            print('no ele to delete')
        else:
            temp=DLL.head
            print('the deleted item:',temp.data)
            '''p=temp
            temp=temp.next
            DLL.head=temp
            temp.prev=None
            del p'''
            DLL.head=temp.next
            temp.next.prev=None
            del temp
    def deleteatloc(self):
        if DLL.head==None:
            print('no ele to delete')
        else:
            x=int(input('enter the ele to be delted:'))
            temp=DLL.head
            while temp.data!=x:
                p=temp
                temp=temp.next
            p.next=temp.next
            temp.next.prev=p
            del temp
    def deleteatend(self):
        if DLL.head==None:
            print('no ele to delete')
        else:
            temp=DLL.head
            while temp.next!=None:
                p=temp
                temp=temp.next
            p.next=None
            temp.prev=None
            del temp
            
    def display(self):
        if DLL.head==None:
            print('no ele to display')
        else:
            temp=DLL.head
            while temp!=None:
                print(temp.data,end='--->')
                temp=temp.next
ob=DLL()
while True:
    print()
    print("1 to insert at begin")
    print("2 to insert at end")
    print("3 to insert at spec loc")
    print("4 to deleteatbeg")
    print("5 to display")
    print("6 to delete at spec loc")
    print("7 to delete at end")
    print("8 to exit")
    ch=int(input("What do you want!!!"))
    if ch==1:
        ob.insertatbeg()
    elif ch==2:
        ob.insertatend()
    elif ch==3:
        ob.insertatloc()
    elif ch==4:
        ob.deleteatbeg()
    elif ch==5:
        ob.display()
    elif ch==6:
        ob.deleteatloc()
    elif ch==7:
        ob.deleteatend()
    elif ch==8:
        break
    else:
        print('invalid option')

