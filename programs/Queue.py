class Queue:
    def __init__(self):
        self.queue = []
        self.size = 5
        self.front = 0
        self.rear = 0

    def enqueue(self, x):
        if self.rear == self.size:
            print("Queue is Full")
        else:
            self.queue.append(x)
            self.rear += 1

    def dequeue(self):
        if self.rear == self.front:
            print("Queue is Underflow")
        else:
            print(f"Element to be deleted: {self.queue[self.front]}")
            self.front += 1

    def display(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            print(f"{self.queue[self.front]} <-- front")
            for i in range(self.front + 1, self.rear-1):
                print(self.queue[i])
            print(f"{self.queue[self.rear - 1]} <-- rear")


obj = Queue()
while True:
    print("-----*--Queue Menu--*-----")
    print("1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        x = int(input("Enter element:"))
        obj.enqueue(x)
    elif ch == 2:
        obj.dequeue()
    elif ch == 3:
        obj.display()
    elif ch == 4:
        break
    else:
        print("Invalid Choice")
