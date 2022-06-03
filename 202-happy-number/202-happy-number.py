class Solution:
    def isHappy(self, n: int) -> bool:
        prev_sums = set()
        sum_all_digital = n
        while sum_all_digital not in prev_sums:
            prev_sums.add(sum_all_digital)
            sum_all_digital = self.sum_square(sum_all_digital)
            if sum_all_digital == 1:
                return True
        return False

    def sum_square(self, n: int) -> int:
        output = 0

        while n:
            div, mod = divmod(n, 10)
            output += mod**2
            n = div

        return output