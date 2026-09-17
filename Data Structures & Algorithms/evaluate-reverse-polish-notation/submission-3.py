class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        holder = []


        for t in tokens:
            if t not in ["+","-","/","*"]:
                holder.append(int(t))
            else:
                b = holder.pop()
                a = holder.pop()
                if t == "+":
                    holder.append(a+b)
                if t == "-":
                    holder.append(a-b)
                if t == "*":
                    holder.append(a*b)
                if t == "/":
                    holder.append(int(a/b))
        return holder[-1]
        