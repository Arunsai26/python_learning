# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
        
#         n=len(nums)
#         k=k%n
        
#         rev(nums,0,k-1)
#         rev(nums,k,n-1)
#         rev(nums,0,n)


# def rev(nums,start,end):
#         while(start<=end):
#             temp=nums[start]
#             nums[start]=nums[end]
#             nums[end]=temp
#             start+=start
#             end=end-1    


    