class Solution:
    def is_eat(self,piles,h,m):
        count=h
        for i in piles:
            count-=(i//m)+1
            if (i//m)==(i/m):
                count+=1
        if count>=0:
            return True
        return False 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result=0
        l=1
        r=sum(piles)
        while l<=r:
            m=(l+r)//2
            if self.is_eat(piles,h,m):
                r=m-1
                result=m
            else:
                l=m+1
        return result