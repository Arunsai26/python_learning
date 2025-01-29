class Solution:
    def bs(self,arr,target):
        start,end=0,len(arr)-1
        while start<=end:
            mid=start+end//2
            if mid==target:
                return mid
            elif mid>target:
                end=mid-1
            else:
                start=mid+1
    class Ano:
        def __init__(self,arr):
            self.arr=arr

            
        def other(self):
            sol=Solution()
            self.bin=sol.bs(self.arr,5)
            return self
            


arr = [1, 2, 3, 4, 5, 6, 7, 8] 
ano=Solution.Ano(arr)
result=ano.other()    
print(result)
        
        
    

        
            