class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        list_num = []

        while n != 0:
            list_num.append(n % 10)
            n //= 10
        list_num.reverse()
        list_num = self.helper(list_num)
        return self.convertToInteger(list_num)

    def helper(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums

        updatedSubList = self.helper(nums[1:len(nums)])
        updatedSubList.insert(0, nums[0])
        print(updatedSubList)
        nums = updatedSubList

        if nums[0] > nums[1]:
            nums[0] -= 1
            for i in range(1, len(nums)):
                nums[i] = 9

        return nums

    def convertToInteger(self, nums):
        n = 0
        for num in nums:
            n = n * 10 + num
        return n