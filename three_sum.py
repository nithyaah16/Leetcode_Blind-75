class Solution:
    def threeSum(self, nums: list[int]) -> list[List[int]]:
        nums.sort()
        res= []

        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l,r = i+1, len(nums)-1

            while l<r:
                total = a + nums[l] + nums[r]
                if total ==0:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                
                elif total < 0:
                    l+=1
                elif total > 0:
                    r-=1
        return res        

            
            