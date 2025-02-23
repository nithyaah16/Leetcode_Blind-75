class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        cur_min , cur_max = 1,1

        for n in nums:
            if n == 0:
                cur_min , cur_max = 1,1
                continue
            temp = n*cur_max
            cur_max = max(n*cur_max,n*cur_min, n)
            cur_min = min(temp,n*cur_min, n)
            res = max(res,cur_max)
        return res
