

letters = ["c","f","j"]
target = "c"


ans=[]

for i in range(len(letters)):
    if letters[i]>target:
        ans.append(letters[i])
       
    
if len(ans)>1:
    print(str(min(ans)))
else:
    print(str(letters[0]))


    









   
    

    
        