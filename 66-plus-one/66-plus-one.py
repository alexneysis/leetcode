class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            div, mod = divmod(digits[i], 10)
            digits[i] = mod
            if div == 0:
                return digits

        digits.insert(0, 1)
        return digits