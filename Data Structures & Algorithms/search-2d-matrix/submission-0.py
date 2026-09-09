class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        s=len(matrix[0])
        r=(len(matrix)*s)-1
        while l<=r:
            m=(l+r)//2
            ind=m//s
            ind1=m%s
            if matrix[ind][ind1]==target:
                return True
            elif matrix[ind][ind1]>target:
                r=m-1
            else:
                l=m+1
        return False