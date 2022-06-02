class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        max_volume = 0
        while l < r:
            volume = (r - l) * min(height[l], height[r])
            max_volume = max(max_volume, volume)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_volume