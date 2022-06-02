class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key_nums = dict()

        for i, v in enumerate(nums):
            if target - v in key_nums:
                return [i, key_nums[target - v]]
            key_nums[v] = i
    