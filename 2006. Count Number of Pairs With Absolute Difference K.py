class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0
        for i in range(len(nums)):
            diff_one = nums[i] - k
            diff_two = nums[i] + k

            list_one = hashmap.get(diff_one)
            # falsy syntax
            if list_one:
                count += len(list_one)

            list_two = hashmap.get(diff_two)
            if list_two:
                count += len(list_two)

            i_list = hashmap.get(nums[i])
            if i_list:
                i_list.append(i)
                hashmap[nums[i]] = i_list
            else:
                hashmap[nums[i]] = [i]

        return count