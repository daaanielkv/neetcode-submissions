class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_sum = [nums[0]] * len(nums)
        suffix_sum = [nums[len(nums) - 1]] * len(nums)

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] * nums[i]
            suffix_sum[- 1 - i] = suffix_sum[- i] * nums[- 1 - i]

        res = [suffix_sum[1]]
        for i in range(1, len(nums) - 1):
            res.append(prefix_sum[i - 1] * suffix_sum[i + 1])
        res.append(prefix_sum[- 2])

        return res