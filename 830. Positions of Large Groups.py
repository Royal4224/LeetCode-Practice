class Solution:
    def largeGroupPositions(self, s: str):
        output = []
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[i] == s[j]:
                j += 1
            if j - i >= 3:
                output.append([i, j - 1])
            i = j

        return output
