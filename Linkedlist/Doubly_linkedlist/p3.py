class Node:
    def __init__(self,value,next=None,back=None):
        self.data=value
        self.next=next
        self.back=back
class LinkedList:
    def arrayt0link(self,arr):
        self.head=Node(arr[0])
        prev=self.head
        for i in range(1,len(arr)):
            temp=Node(arr[i],None,prev)
            prev.next=temp
            prev=prev.next
        return self.head
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        return self.head
    def delete_head(self):
        if self.head==None or self.head.next==None:
            return None
        prev=self.head
        self.head=self.head.next
        self.head.back=None
        prev.next=None
    def Delete_tail(self):
        if self.head==None or self.head.next==None: return None
        tail=self.head
        while tail.next is not None:
            tail=tail.next
        prev=tail.back
        tail.back=None
        prev.next=None    
        return self.head
    def Del_kele(self,item):
        if self.head==None:return None
        count=0
        temp=self.head
        
        while temp is not None:
            count=count+1
            if count==item:break
            temp=temp.next
        prev=temp.back
        front=temp.next
        if prev==None or front==None:return None
        elif prev==None:self.delete_head()
        elif front==None:self.Delete_tail()
        else:
            prev.next=front
            front.back=prev
            temp.next=None
            temp.back=None
            return self.head
    def Delete_node(self,temp):

        prev=temp.back
        front=temp.next
        if front==None:
            prev.next=None
            temp.back=None
        else:
            prev.next=None
            front.back=None

        temp.back,temp.next=None,None
    def insert_at_head(self,value):
        new_node=Node(value,self.head,None)
        self.head.back=new_node
        self.head=new_node
    def insert_at_tail(self,value):
        if self.head==None:
            return self.insert_at_head()
        tail=self.head
        while tail.next is  not  None:
            tail=tail.next
        prev=tail.back
        new_node=Node(value,tail,prev)
        prev.next=new_node
        tail.back=new_node
    def inser_at_kthele(self,value,item):
        if item==1:
            return self.insert_at_head()
        temp=self.head
        count=0
        while temp.next is not None:
            count+=1
            if count==item:break
            temp=temp.next
        prev=temp.back
        new_node=Node(value,temp,prev)
        prev.next=new_node
        temp.back=new_node

    def insert_at_Node(self,temp,value):
        prev=temp.back
        new_node=Node(value,temp,prev)
        prev.next=new_node
        temp.back=new_node
    
    def reverse(self):
        if self.head is None or self.head.next is None:
            return self.head  # If the list is empty or has only one node, return it as is
    
        current = self.head
        prev = None
        
        # Traverse the list and reverse the pointers
        while current is not None:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the direction of the next pointer
            current.back = next_node  # Reverse the direction of the back pointer
            
            prev = current  # Move prev to current
            current = next_node  # Move to the next node
        
        # After the loop, prev will be at the new head of the list
        self.head = prev
        return self.head









        

    




        

        










        
        
    


            
            












LL=LinkedList()
arr=[1,2,3,4]
LL.arrayt0link(arr)
# node_to_deelte=LL.head.next
# LL.Delete_node(node_to_deelte)
# LL.insert_at_head(10)
# LL.insert_at_tail(50)
# LL.inser_at_kthele(90,2)
# node_to_insert=LL.head.next
# LL.insert_at_Node(node_to_insert,100)
LL.reverse()
LL.traverse()






    
        
        