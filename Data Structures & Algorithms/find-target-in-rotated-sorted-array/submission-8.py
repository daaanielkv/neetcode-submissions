class Solution:
    def search(self, nums: list[int], target: int) -> int:
              
        l = 0
        r = len(nums) - 1
        n = len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        m = l

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            current = (mid + m) % n
            print(mid, current)
            if nums[current] == target:
                return current
            elif nums[current] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1