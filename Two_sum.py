from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist_prev = {}
        for i,n in enumerate (nums):
            diff = target - n
            if diff in exist_prev:
                return (exist_prev[diff], i)
            exist_prev[n] = i
        return
            
        