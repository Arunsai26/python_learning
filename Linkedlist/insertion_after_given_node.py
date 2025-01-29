class Node:
    def __init__(self,val,next):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,val):
        new_node=Node(val)
        new_node.next=self.head
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
    def Traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="")
        temp=temp.next
    


L=LinkedList()
L.insert(12)
L.insert(13)
L.insert(14)
L.insert(15)
L.Traverse()



        





        


        

        