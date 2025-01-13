class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            for i,v in enumerate(nums):
                if v==target:
                    return i
        else:
            return -1
            
