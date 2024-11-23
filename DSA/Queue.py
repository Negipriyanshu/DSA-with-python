class Queue:
    def __init__(self,item):
        self.item=[]
        self.front=None
        self.rear=None
    def is_empty(self):
        return len(self.item)==0
    def enqueue(self,data):
        self.item.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.item.pop(0)
        else:
            raise IndexError("Queue is underflow...")
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError("Queue is underflow...")     
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Queue is underflow...")
    def Size(self):
        if self.is_empty():
            raise IndexError("Queue is underflow")
        else:
            return len(self.item)
        