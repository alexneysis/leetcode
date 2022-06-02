class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        basket_letters = set()
        longest_word = 0
        l = 0

        for r in range(len(s)):
            while s[r] in basket_letters:
                basket_letters.remove(s[l])
                l += 1
            basket_letters.add(s[r])
            longest_word = max(longest_word, r - l + 1)

        return longest_word