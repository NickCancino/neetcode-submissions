class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        
        if strs == "":
            return [""]
        for word in strs:
            keys = tuple(sorted(word))
            if keys not in groups:
                groups[keys] = []
                groups[keys].append(word)
            else:
                groups[keys].append(word)
        
                
        
        return list(groups.values())