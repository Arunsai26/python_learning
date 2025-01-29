class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,value):
        # create a new node with the help of above created Node class method
        new_node=Node(value)
        # assign address of new_node to the head node
        new_node.next=self.head
        # reassign the head to newnode
        self.head=new_node
    def Atmiddle(self,prev_data,new_data):
        prev=self.head

        while prev is not None:
            if prev.data==prev_data:
                break
        prev=prev.next

        if prev is None:
            print("Node not found")
        else:
            new_node=Node(new_data)
            new_node.next=prev.next
            prev.next=new_node
    def End(self,value):
        new_Node=Node(value)
        if self.head is None:
            self.head=new_Node
        
        else:
            tail=self.head
            while tail.next is not None:
                tail=tail.next
            tail.next=new_Node

            
        
        
        
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next


L=LinkedList()
L.insert(4)
L.insert(10)
L.insert(12)
L.insert(5)
L.Atmiddle(10,2)

L.End(2)



L.traverse()








        


   
    