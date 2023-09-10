class Queue:
    def __init__(self):
        self.size = 5
        self.front = 0
        self.rear = 0
        self.Q = []

    def insert(self, e):
        if self.rear == self.size:
            print("Queue is Full")
        else:
            self.Q.append(e)
            self.rear += 1

    def delete(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            print("Element to be deleted is", self.Q[self.front])
            self.front += 1

    def display(self):
        if self.front == self.rear:
            print("No elements to display")
        else:
            print(self.Q[self.front], "<-- front")
            for i in range(self.front + 1, self.rear-1):
                print(self.Q[i])
            print(self.Q[self.rear - 1], "<-- rear")

queueObj = Queue()

while True:
    print("Queue Menu")
    print("-----------")
    print("1 for insert")
    print("2 for delete")
    print("3 for display")
    print("4 for exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        x = int(input("Enter the element to be inserted: "))
        queueObj.insert(x)
    elif ch == 2:
        queueObj.delete()
    elif ch == 3:
        queueObj.display()
    elif ch == 4:
        break
    else:
        print("Invalid choice")


