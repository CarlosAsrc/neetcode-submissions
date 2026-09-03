class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = 0
        t = len(heights)-1
        res = 0
        while h < t:
            v = min(heights[h], heights[t]) * (t - h)
            res = max(res, v)
            if heights[h] > heights[t]:
                t -= 1
            else:
                h += 1
        return res
        