class Solution:
    def isValid(self, s: str) -> bool:

        temp = []

        for i in s:
            if i == "(" or i == "{" or i == "[":
                temp.append(i)
            else:
                if not temp:
                    return False
                if i == ")" and temp.pop() != "(":
                    return False
                if i == "}" and temp.pop() != "{":
                    return False
                if i == "]" and temp.pop() != "[":
                    return False
        return len(temp) == 0


                
     