class Solution:
    def twoSum(self, nums, target: int):
        d = {}
        for i, num in enumerate(nums):
            second_num = target - num
            d[num] = second_num
            if (second_num in d):
                second_num_i = nums.index(second_num)
                # disallow num reuse
                if (i != second_num_i):
                    return [i, second_num_i]

        print('done')


sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
