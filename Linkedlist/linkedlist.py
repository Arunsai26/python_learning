class Node:
    # create a constructor which consits of value and address of next node
    def __init__(self,val,next=None):
        self.data=val
        self.next=None

A=Node(10)
B=Node(20)
C=Node(30)

# gives out the address where it is stored in the heap
print("Address")
print(A)
print(B)
print(C)
# gives out data of Node 
print("Value")

print(A.data)
print(B.data)
print(C.data)

# create out a link between A ,B and C 
# we do it by 
A.next=B
B.next=C
C.next=None

# check that here B is linked with C with help of .next 
# where B.next address is equal to C
print(B.next)
print(C)










        



