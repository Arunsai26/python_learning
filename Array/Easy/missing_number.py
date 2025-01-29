arr=[1,2,4,5]
xor1=0
xor2=0
n=5
for i in range(n-1):
    xor2=xor2^i
    xor1=xor1^i+1
xor1=xor1^n
ans=xor1^xor2
print(ans)
