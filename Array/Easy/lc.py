nums=[1,2,3]
k=2
l,temp=0,0
for r in range(len(nums)):
    temp=temp^nums[r]

    if r-l==1:
        temp=temp&nums[r]
        l+=1
    

    
