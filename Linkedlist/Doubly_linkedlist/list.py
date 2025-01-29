

class LinkedList:
    class Node:
        def __init__(self,value,next=None,back=None):
            self.data=value
            self.next=next
            self.back=back
    def arrt_to_doubly(self,arr):
        self.head=self.Node(arr[0])
        prev=self.head
        for i in range(1,len(arr)):
            temp=self.Node(arr[i],None,prev)
            prev.next=temp
            prev=prev.next
        return self.head
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
    def Delete_head(self):
        if self.head==None or self.head.next==None:return None
        prev=self.head
        self.head=self.head.next
        self.head.back=None
        prev.next=None
        return self.head
    def Delete_tail(self):
        if self.head==None or self.head.next==None: return None
        tail=self.head
        while tail.next is not None:
            tail=tail.next
        prev=tail.back
        tail.back=None
        prev.next=None    
        return self.head
    def Kthele(self,k):
        if self.head ==None :return None
        count=0
        temp=self.head
        while temp is not None:
            count+=1
            if count==k:break
            temp=temp.next
        prev=temp.back
        front=temp.next

        if prev==None and front==None:return None
        elif prev==None:return self.Delete_head()
        elif front==None:return self.Delete_tail()
        else:
            prev.next=front
            front.back=prev
            temp.next=None
            temp.back=None
            return self.head
    def inserathead(self,value):
        # print("hello")
        if self.head ==None:
            self.head=self.Node(value)
        else:
            new_node=self.Node(value,self.head,None)
            self.head.back=new_node
            self.head=new_node
    def insert_at_tail(self,value):
        if self.head==None:
            return self.inserathead()
        else:
            tail=self.head
            while tail.next is not None:
                tail=tail.next
            prev=tail.back
            new_node=self.Node(value,tail,prev)
            prev.next=new_node
            tail.back=new_node
            return self.head
    def insert_before_kthele(self,value,k):
        if k==1:
            return self.inserathead()
        temp=self.head
        count=0
        while temp is not None:
            count+=1
            if count==k:break
            temp=temp.next
        prev=temp.back
        new_node=self.Node(value,temp,prev)
        prev.next=new_node
        temp.back=new_node
        return self.head
    def before(self,target_Node,value):
        prev=target_Node.back
        new_node=self.Node(value,target_Node,prev)
        prev.next=new_node
        target_Node.next=new_node
        





        

        
            
        



            
        
















LL=LinkedList()
arr=[1,3,2,4]
LL.arrt_to_doubly(arr)
# LL.Delete_head()
# LL.Delete_tail()
# LL.Kthele(2)
# LL.Kthele(1)
LL.inserathead(20)
LL.insert_at_tail(50)
LL.insert_before_kthele(90,3)
LL.head=LL.Node(20)
node_20=LL.Node(30)
LL.head.next=node_20
node_20.back=LL.head
LL.before(node_20,30)

LL.traverse()

    

        