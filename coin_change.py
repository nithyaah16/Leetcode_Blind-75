class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0:0}
        def min_coins(amt):
            if amt in memo:
                return memo[amt]
            minn = float('inf')
            for coin in coins:
                diff = amt - coin
                if diff < 0 :
                    break
                minn = min(minn,(min_coins(diff))+1)
            memo[amt] = minn
            return minn
        
        if min_coins(amount) < float('inf') :
            return min_coins(amount)
        else:
            return -1
