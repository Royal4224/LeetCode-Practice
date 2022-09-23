class Solution:
    def concatenatedBinary(self, n: int) -> int:
        total_sum, _ = self.helper(n)

        return total_sum

    def helper(self, n):
        if n == 1:
            return 1, 2

        prev_sum, power = self.helper(n - 1)

        if n >= power:
            power *= 2

        total_sum = int((prev_sum * power + n) % 1000000007)

        return total_sum, power

## while i != 0:
##    s = s + (i % 2)
##    i // 2