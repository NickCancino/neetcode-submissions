class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #else return 0
        l, maxprof = 0,0

        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1
            maxprof = max(maxprof, prices[r]-prices[l])

    
        return maxprof
        