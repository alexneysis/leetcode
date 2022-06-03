class Solution:
    def isHappy(self, n: int) -> bool:
        sum_all_digital = n
        for i in range(100):
            sum_all_digital = sum(map(lambda x: int(x)**2, list(str(sum_all_digital))))
            print(sum_all_digital)
            if sum_all_digital == 1:
                return True
        return False