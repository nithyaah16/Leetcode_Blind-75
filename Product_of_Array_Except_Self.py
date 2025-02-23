class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l_prod = 1
        r_prod = 1
        answer = [1] * n

        for i in range(n):
            answer[i] *= l_prod
            l_prod *= nums[i]
        
        for i in range(n-1,-1,-1):
            answer[i] *= r_prod
            r_prod *= nums[i]
        
        return answer