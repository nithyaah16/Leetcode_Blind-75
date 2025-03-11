class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def helper(nums):
            prev,curr = 0,0
            for n in nums:
                total = max(prev+n,curr)
                prev = curr
                curr = total
            return curr
        
        return max(nums[0],helper(nums[1:]),helper(nums[:-1]))
