class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,head=None):
        self.head=None
    def is_empty(self):
        return self.head==None
    def insert_at_start(self,data):
        n=Node(data,self.head)
        self.head=n
    def insert_at_last(self,data):
        temp=self.head
        n=Node(data)
        if temp is not None:
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.head=n
    def insert_at_node(self,data,search):
        temp=self.head
        if temp is None:
            print("singly linklist is empty...")
        else:
            while temp is not None:
                if search == temp.item:
                    n=Node(data,temp.next)
                    temp.next=n 
                    break
                else:
                    temp=temp.next
    def traverse(self):
        temp=self.head
        if temp is None:
            print("linklist is empty...")
        else:
            while temp is not None:
                print(temp.item,end=' ')
                temp=temp.next
    def delete_first(self):
        if self.head is None:
            print("list is empty...")
        else:
            self.head=self.head.next
    def delete_last(self):
        temp=self.head
        if self.head is None :
            pass
        elif self.head.next is None:
            self.head=self.head.next
        else:
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_specified_element(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start=None
        else:
            temp=self.start
            if temp.item ==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next==temp.next.next
                        break
                    temp=temp.next
my_list = SLL()
my_list.insert_at_start(20)
my_list.insert_at_start(35)
my_list.insert_at_last(50)
my_list.insert_at_node(search=35,data=24)
my_list.traverse()