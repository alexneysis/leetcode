class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        freq = [[] for i in range(len(nums) + 1)]
        for key, val in counter.items():
            freq[val].append(key)

        result = []
        for i in reversed(freq):
            for n in i:
                result.append(n)
                if len(result) == k:
                    return result