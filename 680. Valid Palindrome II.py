class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                left_sub = self.checkPalindrome(s[l:r])
                right_sub = self.checkPalindrome(s[l + 1:r + 1])

                if left_sub or right_sub:
                    return True
                else:
                    return False
            l += 1
            r = len(s) - 1 - l
        return True

    def checkPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[len(s) - 1 - l]:
                return False

            l += 1
            r = len(s) - 1 - l

        return True