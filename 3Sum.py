class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[] #list
        nums_s=sorted(nums)
        #print(nums_s)
        for i in range(len(nums_s)-2):
           # if len(nums_s)==3:
            #    if nums_s[0]+nums_s[1]+nums_s[2]==0:
             #       ans.append([nums_s[0],nums_s[1],nums_s[2]])
              #      break
            if nums_s[i]==nums_s[i-1] and i!=0:
                continue
            l=i+1
            r=len(nums_s)-1 
            #print(f"initial i {i} l {l} and r {r}")           
            while r>l:
                if nums_s[i]+nums_s[l]+nums_s[r]<0:
                    l=l+1
                    #print(f"updated l {l}")
                elif nums_s[i]+nums_s[l]+nums_s[r]>0:
                    r=r-1
                #    print(f"updated r {r}")
                else:
                    ans.append([nums_s[i],nums_s[l],nums_s[r]])
                #    print(f"added {ans}")
                    l+=1
                    while nums_s[l]==nums_s[l-1] and r>l:
                        l+=1      
        return ans
           

