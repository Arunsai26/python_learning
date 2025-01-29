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
    def inseratlast(self,value):
        new_node=Node(value)
        if self.head==None:
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

        

    
    def dels(self):
        if self.head is None:
            print("node is not there")
            return self.head
        else:
            self.head=self.head.next
            return self.head
    def last(self):
        temp=self.head
        if temp==None or temp.next==None :
            return None

      

        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
        # return self.head
    def kthele(self,k):
        if self.head==None : return None
        if k==1:
            self.head=self.head.next
            return self.head
        count=1
        temp=self.head
        prev=None
        while temp is not None :
            
            if count ==k:
                prev.next=prev.next.next
                break
            prev=temp
            temp=temp.next
            count+=1
        return self.head
    
    def removeElement(self,item):
        if self.head is None: print("list is empty")
        if self.head.data ==item : self.head=self.head.next
        temp=self.head
        prev=None
        while temp is not None:
            if temp.data==item:
                prev.next=prev.next.next
                break
            prev=temp
            temp=temp.next
        

            

        

        


    
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        
    
        



LL=LinkedList()
LL.insert(10)
LL.insert(20)
LL.insert(30)
LL.insert(40)
# LL.kthele(3)
# LL.kthele(1)
# LL.kthele(4)
# LL.removeElement(10)
# LL.removeElement(30)
# LL.removeElement(90)
LL.inseratlast(50)
LL.middle(20,70)
LL.traverse()








