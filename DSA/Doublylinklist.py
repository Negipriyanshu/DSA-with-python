class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,head=None):
        self.head=head

    def is_empty(self):
        return self.head==None
    
    def insert_at_rear(self,data):
        n=Node(None,data,self.head)
        if not self.is_empty():
            self.head.prev=n
        self.head=n
    def insert_at_end(self,data):
        n=Node(self.prev ,data,None)
        temp=self.head
        if self.head is not None:
            while temp.next is not None:
                temp=temp.next        
        n=Node(temp,data,None)
        if temp==None:
            self.head=n
        else:
            temp.next=n
    def search(self,data):
        temp=self.head
        while temp is not None:
            if temp==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,data,temp):
        if temp!=None:
            n=Node(temp,data,self.head.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
    def traverse(self,data):
        temp=self.head
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
    def delete_from_rear(self):
        if self.head is None:
            pass
        elif self.head is  not None:
            self.head=self.head.next
            if self.head is not None:
                self.head=None
    def delete_from_last(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
    def delete_after(self,data):
        if self.head is None:
            pass
        elif self.head.next is None:
            if self.head.item==data:
                self.head=None
        else:
            temp = self.head
            if temp.item==data:
                self.head=temp.next
                temp.prev.next=None
            else:
                while temp is not None:
                    if temp.item == data:
                        if temp.next is not None:
                            temp.next.prev=temp.prev
                        elif temp.prev is not None:
                            temp.prev.next=temp.next
                        else:
                            self.head=temp.next
                            break
                        temp=temp.next
list1=DLL()
list1.insert_at_rear(50)
list1.insert_after(list1.search(60),20)
list1.insert_at_end(60)
list1.insert_at_rear(55)
list1.insert_after(list1.search(55),44)
list1.traverse()