arr=[1,2,3,1,1,1,1,3,3]
def longest_subarray(arr,k):
    i=0
    j=0
    sum=arr[0]
    maxlen=0
   
    while(j<len(arr)):
        while(sum>k and i<=j):
            sum-=arr[i]
            i+=1
        if(sum==k):
            maxlen=max(maxlen,j-i+1)
        j+=1
        if(j<len(arr)):sum+=arr[j]
    return maxlen
             
            
        

           
        
