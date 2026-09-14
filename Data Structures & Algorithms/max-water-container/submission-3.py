class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea= 0
        currentarea = 0
        length = 0
        lower = 0
        z,x= 0,len(heights)-1

        while z < x:
            length = x - z
            lower = min(heights[z], heights[x])

            if heights[z] > heights[x]:
                x-=1
            elif heights[z] <heights[x]:
                z+=1
            else:
                z+=1

            currentarea = lower*length
            maxarea=max(currentarea,maxarea)
        return maxarea
            
