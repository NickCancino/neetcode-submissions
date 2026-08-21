class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nmap = {}
        for n in nums:
            if n not in nmap:
                nmap[n] = 1
            else:
                nmap[n]+=1

        return sorted(nmap, key=nmap.get)[-k:]