class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        
        while l <= r:
            rate = (l+r) // 2
            timetofinish = 0
            for pile in piles:
                timetofinish += math.ceil(pile / rate)
            if timetofinish > h:
                l = rate + 1
            else:
                r = rate - 1
        return l



        