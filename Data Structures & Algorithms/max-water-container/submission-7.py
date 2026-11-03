class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R, maximum = 0, len(heights) - 1, 0
        while L < R: 
            area = (R - L) * min(heights[L], heights[R])
            maximum = max(area, maximum)
            if heights[L] < heights[R]:
                L += 1
            else: 
                R -= 1
        return maximum 