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
a.insert_at_beg(7)
a.insert_at_beg(15)
a.delete_at_end()
a.delete_at_end()
a.print()
