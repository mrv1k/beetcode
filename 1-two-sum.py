class Solution:
    def twoSum(self, nums, target: int):
        d = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                second_num_i = nums.index(diff)
                return [i, second_num_i]
            d[num] = diff


sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
