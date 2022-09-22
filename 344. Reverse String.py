class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            left_c = s[l]
            right_c = s[r]
            temp = right_c
            s[r] = left_c
            s[l] = temp
            l += 1
            r = len(s) - 1 - l
