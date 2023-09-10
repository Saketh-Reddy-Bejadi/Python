class BST:
    def __init__(self, val=None, left=None, right=None):
        self.left = left  # left child
        self.right = right  # right child
        self.val = val  # root node
    
    def insert(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is not None:
                    self.left.insert(val)
                else:
                    self.left = BST(val)
            else:
                if self.right is not None:
                    self.right.insert(val)
                else:
                    self.right = BST(val)
        else:
            self.val = val
    
    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals
    
    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals
    
    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

ob = BST()
print("TREE TRAVERSALS\n1. Insert\n2. Preorder\n3. Inorder\n4. Postorder\n5. break")

while True:
    ch = int(input("Enter your choice: "))
    if ch == 1:
        data = int(input("Enter the element: "))
        ob.insert(data)
    elif ch == 2:
        print("PREORDER: ", ob.preorder([]))
    elif ch == 3:
        print("INORDER: ", ob.inorder([]))
    elif ch == 4:
        print("POSTORDER: ", ob.postorder([]))
    elif ch == 5:
        break
    else:
        print("INVALID CHOICE")
