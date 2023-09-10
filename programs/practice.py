Null=None
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=Null
        
node1=Node(10)
node2=Node(20)
node1.ref=node2
print(node1.data," ", node1.ref)
node2.ref=Null
print(node2.data," ",node2.ref)