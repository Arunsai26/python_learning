# s=set()
# union=[]
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]
# n1=len(arr1)
# n2=len(arr2)
# for i in arr1:
#     s.add(i)
# for i in arr2:
#     s.add(i)
# for num in s:
#     union.append(num)
# print(union)

union=[]

i=0
j=0
while(i<len(arr1) and j<len(arr1)):
    if(arr1[i]<=arr2[j]):
        if( len(union)==0 or union[-1]!=arr1[i]):
            union.append(arr1[i])
        i+=1
    else:
        if(arr2[j]<=arr1[i]):
            if(len(union)==0 or union[-1]!=arr2[j]):
                union.append(arr2[j])
            j+=1
while(i<len(arr1)):
        if( len(union)==0 or union[-1]!=arr1[i]):
            union.append(arr1[i])
        i+=1
    
while(j<len(arr2)):
   
            if(len(union)==0 or union[-1]!=arr2[j]):
                union.append(arr2[j])
            j+=1

print(union)





