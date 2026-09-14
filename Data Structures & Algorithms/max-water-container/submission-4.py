class Solution:
    def maxArea(self, heights: List[int]) -> int:
        z,x= 0,len(heights)-1
        maxarea = 0
        while z < x:
            area = (x-z) * min(heights[z],heights[x])
            maxarea=max(area,maxarea)
            if heights[z] > heights[x]:
                x-=1
            else:
                z+=1

        return maxarea
            
