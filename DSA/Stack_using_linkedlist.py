class Node :
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Stack:
    def __init__(self,head=None):
        self.head=head
    
    def is_empty(self):
        return self.head == None
    
    def push(self,data):
        n=Node(data)
        if self.is_empty():
            self.head=n
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=n
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty...")
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def Seek(self):
        if self.is_empty():
            raise IndexError("Stack is empty...")
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            return temp.item
    def Size(self):
        if self.head==None:
            raise IndexError("Stack is empty...")
        else :
            temp=self.head
            count=0
            while temp is not None:
                temp=temp.next
                count= count+1
            return count
stack=Stack()
stack.push(50)
stack.push(90)
stack.push(69)
print(stack.Seek() , stack.Size())
