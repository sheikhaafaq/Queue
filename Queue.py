class Queue:
    def __init__(self):
        self.items = []  
    def enqueue(self,data):
        self.items.insert(0,data)
    def dequeue(self):
        if not self.isEmpty():
            self.items.pop()
        else:
            print("Queue is Empty..")
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Queue is Empty..")

menu = '''press 1: Enqueue
press 2: Dequeue
press 3: peek\n>>'''
object = Queue()
def UI():
    while True:
        option = input(menu)
        if option == '1':
            object.enqueue(input("Data: "))
        elif option == '2':
            object.dequeue()
        elif option == '3':
            print(object.peek())
        else:
            break
UI()