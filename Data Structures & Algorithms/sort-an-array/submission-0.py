class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        return self.qsort(nums)

    def qsort(self, nums, left=0, right=None):
        
        if right == None:
            right = len(nums) - 1
        
        i, j = left, right
        pivot = nums[(left + right) // 2]

        while i <= j:

            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        if i < right:
            self.qsort(nums, i, right)
        if j > left:
            self.qsort(nums, left, j)

        return nums