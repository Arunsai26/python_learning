i=0
j=0
arr1=[1,2,2,3,3,4,5,6]
arr2=[2,3,4,5,6,6,7]
ans=[]
while(i<len(arr1) and j<len(arr2)):
    if(arr1[i]==arr2[j]):
        ans.append(arr2[i])
        i+=1
        j+=1
        
    elif(arr1[i]<arr2[j]):
        i+=1
    else:
        j+=1
print(ans)    