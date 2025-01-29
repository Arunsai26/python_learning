# optimal solution
arr=[1,1,2,3,3,4,4]
# o/p:2
xor=0
for i in range(len(arr)):
    xor=xor^arr[i]
print(xor)
