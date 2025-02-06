class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li=[]
        nums1=nums.copy()
        while len(li)<2:
            for i in range(len(nums)):
                if nums[i]!=target/2 and target-nums[i] in nums:
                    li.append(i)
                elif nums[i]==target/2: 
                    nums1.remove(nums[i])
                    if nums[i] in nums1:
                        li.append(i)
                        k=i
                        for j in range(k+1,len(nums)):
                            print(k)
                            if nums[i]==nums[j]:
                                li.append(j)

        return li        
        
