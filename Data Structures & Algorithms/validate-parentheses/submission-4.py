class Solution:
    def isValid(self, s: str) -> bool:

        holder = []

        for bracket in range(len(s)):
            if s[bracket] == "{" or s[bracket] =="("or s[bracket] == "[":
                holder.append(s[bracket])
            else:
                if not holder:
                    return False
                if s[bracket] == "}" and holder.pop() != "{":
                        return False
                if s[bracket] == ")" and holder.pop() != "(":
                        return False
                if s[bracket] == "]" and holder.pop() != "[":
                        return False
        return len(holder) == 0

                
     