class Node:
    def __init__(self,value,next=None):
        self.data=value
        self.next=next
class LinkedList:
    def convert(self,arr):
        if not arr:
            return None
        self.head=Node(arr[0])
        curr=self.head

        for value in arr[1:]:
            new_node=Node(value)
            curr.next=new_node
            curr=new_node
        return self.head
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next

LL=LinkedList()
arr=[1,2,3,4,5]
LL.convert(arr)
LL.traverse()

            
        