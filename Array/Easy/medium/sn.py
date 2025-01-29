class Solution:
    def getRow(self, n: int) -> List[int]:
        for c in range(1,n+1):
            print(combo(n-1,c-1),end=" ")
    

ans=1
def combo(n,c):
    print(ans)
    for i in range(n):
        ans=ans*(n-1)
        ans=ans/i
    return ans