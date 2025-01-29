mpp={}
s="test"

for char in s:
    if mpp[char] in mpp:
        mpp[char]+=1
    else:
        mpp[char]=1
for key,value in mpp.items():
    if value>1:
        print(key)
   

  
    
     
