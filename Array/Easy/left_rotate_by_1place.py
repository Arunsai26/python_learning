arr=[1,2,3,4,5]
temp=arr[0]
m=len(arr)
for i in range(1,len(arr)):
    arr[i-1]=arr[i]
arr[m-1]=temp
print(arr)
