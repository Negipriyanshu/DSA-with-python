class Stack(list):
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if self.is_empty():
             raise IndexError("stack is empty...")
        else:
            return super().pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty...")
        else:
            return self[-1]
    def Size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("No attribute 'Insert' in Stack ")
s1=Stack()
s1.push(30)
s1.push(49)
s1.push(29)
print("top element is ", s1.peek())
s1.pop()
print("top element is ", s1.peek())