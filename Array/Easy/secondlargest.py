arr=[1,2,4,7,7,5]
# Largest=arr[0]
# secondLargest=-1
# for i in range(len(arr)):
#     if(arr[i]>Largest):
       
#         secondLargest=Largest
#         Largest=arr[i]
         
#     elif(arr[i]<Largest and arr[i]>secondLargest):
#          secondLargest=arr[i]
# print(secondLargest)
  
# def SecondSmallest(arr):
#     smallest=arr[0]
#     sSmallest=99999
#     for i in range(len(arr)):
#         if(arr[i]<smallest):
#            sSmallest=smallest
#            smallest=arr[i]
#         elif(arr[i]!=smallest and arr[i]<sSmallest):
#             sSmallest=arr[i]
#     print(sSmallest)   

# SecondSmallest(arr)
class Solution:
    def print2largest(self, arr):
        largest=arr[0]
        slargest=-1
        for i in range(len(arr)):
            if(arr[i]>largest):
                slargest=largest
                largest=arr[i]
            elif(arr[i]<largest and arr[i]>slargest):
               slargest=arr[i]
        
        return slargest
        


