class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        out = []
        n = len(nums)
        
        for k in range(n):
            # Пропускаем дубликаты для k
            if k > 0 and nums[k] == nums[k-1]:
                continue
                
            i, j = k + 1, n - 1
            
            while i < j:
                total = nums[k] + nums[i] + nums[j]
                
                if total == 0:
                    out.append([nums[k], nums[i], nums[j]])
                    
                    # Пропускаем дубликаты для i
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    # Пропускаем дубликаты для j
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    
                    i += 1
                    j -= 1
                    
                elif total < 0:
                    i += 1
                else:  # total > 0
                    j -= 1
                    
        return out