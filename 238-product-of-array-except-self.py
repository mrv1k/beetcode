class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = nums[:]
        for i in range(1, len(pre)):
            pre[i] = pre[i - 1] * pre[i]

        post = nums[:]
        for i in range(len(post) - 2, -1, -1):
            post[i] = post[i] * post[i + 1]

        result = nums[:]
        for i in range(len(nums)):
            pre_v = pre[i - 1] if i - 1 >= 0 else 1
            post_v = post[i + 1] if i + 1 < len(nums) else 1

            result[i] = pre_v * post_v

        return result
