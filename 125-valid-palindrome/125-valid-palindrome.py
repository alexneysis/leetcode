class Solution:
    def isPalindrome(self, s: str) -> bool:
        pure_s = "".join((i for i in s.lower() if i.isalnum()))

        return pure_s == pure_s[::-1]
        