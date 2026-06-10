class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        seen_add = seen.add
        for num in nums:
            if num in seen:
                return True
            seen_add(num)
        return False