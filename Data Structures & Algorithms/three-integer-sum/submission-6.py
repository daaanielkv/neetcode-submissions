class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        out = []

        for k in range(len(nums)):

            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i, j = k + 1, len(nums) - 1

            while i < j:

                total = nums[k] + nums[i] + nums[j]

                if total == 0:
                    out.append([nums[i], nums[k], nums[j]])

                    while i < j and nums[i] == nums[i + 1]: 
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1

                    i += 1
                    j -= 1

                elif total < 0:
                    i += 1
                else:
                    j -= 1

        return out


cls = Solution()

res = cls.threeSum([-1,0,1,2,-1,-4])

print(res)