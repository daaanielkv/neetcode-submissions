class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        candidate = nums[0]
        count = 1

        for i in nums[1:]:
            if count == 0:
                candidate = i
            else:
                if i == candidate: count += 1
                else: count -= 1

        return candidate