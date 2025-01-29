# remove duplicates elemensts from an sorted array

arr=[1,1,2,2,2,3,3,3]
# BRUTE FORCE APPROACH
unique=[]
def unique_element(arr):
    unique=len(set(arr))
    print(unique)

unique_element(arr)


# # RETURN NUMBER OF UNIQUE ELEMENTS IN AN SORTED ARRAY
# def two_pointer_approach(arr):
#     i=0
#     for j in range(len(arr)):
#         if(arr[j]!=arr[i]):
#            arr[i+1]=arr[j]
#            i+=1
#     return i+1
# two_pointer_approach(arr)

