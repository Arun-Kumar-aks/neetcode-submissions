class Solution:
    def is_arrange(self,m,n):
        for i in range(m):
            n-=i+1
        return n>=0

    def arrangeCoins(self, n: int) -> int:
        l=0
        r=65536
        result=0
        while l<=r:
            m=(l+r)//2
            if self.is_arrange(m,n):
                result=m
                l=m+1
            else:
                r=m-1    
        return result