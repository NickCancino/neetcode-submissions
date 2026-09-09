class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        if strs == "":
            return ""
        for word in strs:
            key = tuple(sorted(word))
            if key not in groups:
                groups[key]= []
            groups[key].append(word)

        return list(groups.values())


        