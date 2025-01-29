arr=[1,2,1,3,4]
def check(arr):
    for i in range(len(arr)):
        if(arr[i]>=arr[i-1]):
            return True
        else:
            return False
    return True

check(arr)

# class Solution:
#     def check(self, arr: List[int]) -> bool:
#         breaks=0
#         for i in range(len(arr)):
#             if(arr[i-1]>arr[i]):
#                 breaks+=1
#         if(breaks<=1):
#            return True
#         else:
#             return False    
           


     
        