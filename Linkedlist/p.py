class Node:
    def __init__(self,val,next=None):
        self.data=val
        self.next=next



# # created a node 

# A=Node(10)
# B=Node(20)
# C=Node(30)

# print(A)
# print(B)
# print(C)


# # linking in a linked list 

# A.next=B
# B.next=C
# C.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,val):
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        
    def traverse(self,value):
        count=0
        temp=self.head
        while temp!=None:
            # print(temp.data,end=" ")
            if temp.data==value:
                return 1
               
            count=count+1
           
            
            temp=temp.next
        print(count)
    def insert_after(self,prev_data,new_data):
        prev=self.head

        while prev is not None:
            if prev.data==prev_data:
                break
            else:
                prev=prev.next

           
        if prev is None:
            print("Node is not found")
        else:
            new_node=Node(new_data)
            new_node.next=prev.next
            prev.next=new_node
    def insert_end(self,value):

        print("insert at end ")
        new_node=Node(value)

        if self.head is None:
            self.head=new_node
        else:
            tail=self.head

            while tail.next is not None:
                tail=tail.next
            tail.next=new_node
    def Delete_head(self):
        print("head is gone")
        
        if self.head is None:
            print("Node cannot be deleted")
        else:
            self.head=self.head.next
    def Delete_end(self):
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
    def Delete_item(self,item):
        # head
        if self.head.data == item:
            self.head=self.head.next
            return

        temp=self.head
        while temp.next is not None:
            if temp.next.data==item:
                break
            temp=temp.next
        # tail
        if temp.next is None:
            print("node is not found")
        else:
            temp.next=temp.next.next

        
            








    

LL=LinkedList()
LL.insert(10)
LL.insert(20)
LL.insert_after(10,30)
LL.insert_end(50)
LL.Delete_head()
LL.Delete_end()
LL.insert(40)
LL.insert(50)
LL.Delete_item(50)
LL.Delete_item(10)
LL.Delete_item(30)
LL.Delete_item(40)
LL.insert(10)
LL.insert(10)
LL.insert(10)
LL.insert(10)
LL.insert(20)
# LL.Delete_item(10)
result=LL.traverse(20)
if result==1:
    print("value found")
else:
    print("value not found")


        




