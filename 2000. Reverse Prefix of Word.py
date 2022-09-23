class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        string_list = []
        index = None
        for i in range(len(word)):
            if word[i] == ch and index is None:
                index = i
            string_list.append(word[i])

        if index is None:
            return word

        l = 0
        r = index
        while l < r:
            temp = string_list[r]
            string_list[r] = string_list[l]
            string_list[l] = temp
            l += 1
            r = index - l

        reversed_Prefix = ""
        for i in range(len(string_list)):
            reversed_Prefix += string_list[i]

        return reversed_Prefix
    