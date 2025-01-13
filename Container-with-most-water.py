class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res,l,r=0,0,len(height)-1
        while r>l:
            a=(r-l)*min(height[l],height[r])
            res=max(res,a)
            if height[l]>height[r]:
                r=r-1
            else:
                l=l+1
        return res
        
