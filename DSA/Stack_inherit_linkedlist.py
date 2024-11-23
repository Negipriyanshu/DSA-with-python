from SinglyLinklist import *
class Stack(SLL):  #Stack is child class for SLL
    def __init_(self):
        super().__init__()
        self.item_count=0
    def is_empty(self):
        return super().is_empty  # calling the parent class in child classs
    def push(self,data):
        self.insert_at_start(data)
        self.item_count =  self.item_count + 1
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty...")   
        else:
            self.delete_first()
    def seek(self):
        if self.is_empty():
            raise IndexError("Stack is empty...")
        else:
            return self.head.item
    def Size(self):
        return self.item_count
s1=Stack()
s1.push(49)
s1.push(58)
s1.push(78) 
print(s1.seek())       
        