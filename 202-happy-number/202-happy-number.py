class Solution:
    def isHappy(self, n: int) -> bool:
        prev_sums = set()
        sum_all_digital = n
        while sum_all_digital not in prev_sums:
            prev_sums.add(sum_all_digital)
            sum_all_digital = sum(map(lambda x: int(x)**2, list(str(sum_all_digital))))

            if sum_all_digital == 1:
                return True
        return False