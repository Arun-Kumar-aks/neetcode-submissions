class Solution:
    def is_shipped(self,m,days,we):
        count=days
        su=0
        for i in we:
            su+=i
            if su>m:
                count-=1
                su=0
                su+=i
        if count>0:
            return True
        return False

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        result=0
        while l<=r:
            m=(l+r)//2
            if self.is_shipped(m,days,weights):
                result=m
                r=m-1
            else:
                l=m+1
        return result