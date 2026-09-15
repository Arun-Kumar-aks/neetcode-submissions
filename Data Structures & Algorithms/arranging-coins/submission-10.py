class Solution:
    def is_arrange(self,m,n):
        k=m*(m+1)/2
        return k<=n

    def arrangeCoins(self, n: int) -> int:
        l=0
        r=n
        result=0
        while l<=r:
            m=(l+r)//2
            print(m)
            if self.is_arrange(m,n):
                result=m
                l=m+1
            else:
                r=m-1    
        return result