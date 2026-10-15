class Solution:
    def scoreOfString(self, s: str) -> int:
        m = 1
        l = 0
        total = 0
        while m <= len(s)-1:
            total += abs(ord(s[m])-ord(s[l]))
            m +=1
            l += 1
        return total
        
