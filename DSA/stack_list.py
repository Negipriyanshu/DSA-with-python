class Stack:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self.item)==0
    def push(self,data):
        self.item.append(data)
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is empty...")
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self.item)
l1=Stack()
l1.push(50)
l1.push(20)
l1.push(60)
print("Top Element is " ,l1.peek())
l1.pop()
print(l1.peek())