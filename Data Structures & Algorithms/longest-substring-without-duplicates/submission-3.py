class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longestsub = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            

            while count[s[r]] > 1:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l+=1
            longestsub = max(longestsub,r-l+1)
        return longestsub

        pwwkew