class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # sol_1 (4251 ms, 13 mb)

        # n = len(nums)
        # for i in range(n):
        #     for j in range(n):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i, j]
                
        # sol_2

        cache = {}
        for i, val in enumerate(nums):
            cache[val] = i
        for i, val in enumerate(nums):
            diff = target - val
            if diff in cache and i != cache[diff]:
                return [i, cache[diff]]
        
        