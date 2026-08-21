class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        baka = set()

        for num in nums:
            if num in baka:
                return True
            baka.add(num)
        return False