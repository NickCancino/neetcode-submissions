class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for c in nums:
            count[c] =count.get(c,0)+1
            if count[c] > 1:
                return True
        return False
        