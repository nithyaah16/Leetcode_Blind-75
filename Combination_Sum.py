class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack (start , comb , total):
            if total == target:
                res.append(comb.copy())
                return 
            if total > target:
                return 
            
            for i in range(start , len(candidates)):
                comb.append(candidates[i])
                backtrack(i, comb, total+candidates[i])
                comb.pop()

        
        backtrack(0,[],0)
        return res
