class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_a = 0
        stack = []
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                start, v =stack.pop()
                max_a = max(max_a, (i-start)*v)
            stack.append([start, h])

        for height in stack:
            max_a = max(max_a, (len(heights)-height[0])*height[1]   )

        return max_a

        