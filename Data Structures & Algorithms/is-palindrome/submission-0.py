class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        newStr = ''
        for l in s:
            if l.isalnum():
                newStr += l
        return newStr == newStr[::-1]