# The time complexity limit is O(nlogn)
# If we try to solve this problem use simulaton, it will exceed the time limit.
# so, I use two-pointers approach, The core idea is that the area is determined by the shorter wall.
# To increase the area, we need to find a taller wall, so we move the pointer pointing to the shorter wall.
# We place one pointer at the start and the other at the end, and compare the two pointers.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        start, end = 0, len(height) - 1
        while start < end :
            weight = end - start
            if height[start] < height[end] :
                answer = max(answer, weight * height[start])
                start += 1
            else :
                answer = max(answer, weight * height[end])
                end -= 1
        return answer
        