class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        exist_prev = set()
        for i in nums:
            if i in exist_prev:
                return True
            else:
                exist_prev.add(i)
        return False