class Node:
    def __init__(self,value,next=None):
        self.data=value
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
    def end(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            tail=self.head
            while tail.next is not None:
                tail=tail.next
            tail.next=new_node
    def middle(self,prev_data,new_data):
        prev=self.head

        while prev is not None:
            if prev_data==prev.data:
                break
            prev=prev.next
        if prev is None:
            print("Node is not found")
        else:
            new_node=Node(new_data)
            new_node.next=prev.next
            prev.next=new_node

LL=LinkedList()
LL.insert(10)
LL.insert(20)
LL.insert(30)
LL.middle(10,50)
LL.end(40)
LL.traverse()


        
    