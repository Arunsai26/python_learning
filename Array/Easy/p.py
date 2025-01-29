# # r->number of rats present in area
# unit->amount of food each consumes

# # arr number in arr 
# take input 

r=int(input("enter r value:"))
unit=int(input("enter unit value:"))
n=int(input("enter n value:"))

arr = list(map(int, input("Enter food in each house (space-separated): ").split()))




print(arr)

def food_eats(r,unit,arr):
    if len(arr)==0:
         return 0
    count=0
    curr_sum=0
    
    food=r*unit
    for i in range(len(arr)):
        curr_sum=curr_sum+arr[i]
        
    
        if curr_sum>=food:
            return count+1
                
    return count

print("minimum number of houses",food_eats(r,unit,arr))
    
   


        
            


    
 








