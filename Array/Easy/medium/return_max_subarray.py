class Solution:
    def pairWithMaxSum(self, arr):
        sum=0
        maxi=-99999
        ans=-1
        ansend=-1
        for i in range(len(arr)):
            if(sum==0):
                start=i
            
            sum+=arr[i]
            
            if(sum>maxi):
                
                maxi=sum
                ans=start
                ansend=i
            
            if(sum<0):
                sum=0
        for i in range(ans,ansend+1):
            print(arr[i],end=" ")
