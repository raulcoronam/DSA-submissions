class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum, n = 0, len(heights) - 1
        L, R = 0, n 
        actual = 0 
        while L < R:
            actual = (R - L) * min(heights[L], heights[R])
            maximum = max(actual, maximum)
            if heights[L] < heights[R]: 
                L += 1
            else: 
                R -= 1
        return maximum
            


