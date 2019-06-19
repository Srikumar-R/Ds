class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singly():
    def __init__(self):
        self.head=None
    def insert(self,data):
        self.data=data
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def delete(self):
        temp=self.head
        self.head=temp.next
        temp=None
    def print(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
a=Singly()
a.insert(10)
a.insert(5)
a.insert(7)
a.insert(15)
a.delete_at_beg()
a.delete_at_beg()
a.print()
