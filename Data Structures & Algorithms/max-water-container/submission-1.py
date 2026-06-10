class Solution:
    def maxArea(self, heights: list[int]) -> int:

        i, j = 0, len(heights) - 1 

        m = 0

        while i < j:

            delta = j - i
            print(heights[i], heights[j], delta)
            vol = min(heights[i], heights[j]) * delta

            if vol > m: m = vol

            if heights[i] >= heights[j]:
                j -= 1
            else:
                i += 1

        return m