class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singly():
    def __init__(self):
        self.head=None
    def insert_at_beg(self,data):
        self.data=data
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def insert_at_mid(self,data,position):
        self.data=data
        newnode=Node(data)
        temp=self.head
        for i in range(1,position-1):
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    def insert_at_end(self,data):
        self.data=data
        newnode=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    def delete_at_beg(self):
        temp=self.head
        self.head=temp.next
        temp=None
    def delete_at_mid(self,pos):
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        tem=temp.next
        temp.next=tem.next
        tem.next=None
    def delete_at_end(self):
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
    def print(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
a=Singly()
a.insert_at_beg(10)
a.insert_at_beg(5)
a.insert_at_mid(7,2)
a.insert_at_end(15)
a.delete_at_beg()
a.delete_at_mid(2)
a.delete_at_end()
a.print()
