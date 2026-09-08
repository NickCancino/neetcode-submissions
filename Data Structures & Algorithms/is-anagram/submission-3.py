class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        strack = {}
        ttrack = {}
        if len(s) != len(t):
            return False

        for c in s:
            if c not in strack:
                strack[c] = 1
            else:
                strack[c] += 1
        for c in t:
            if c not in ttrack:
                ttrack[c] = 1
            else:
                ttrack[c] += 1
        return strack == ttrack
    