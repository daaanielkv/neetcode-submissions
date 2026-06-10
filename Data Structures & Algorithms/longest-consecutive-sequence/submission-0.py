class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_set = set(nums)
        vars = []

        for i in nums_set:
            if i - 1 not in nums_set:
                vars.append(i)

        max_k = 0
        for start in vars:
            j = 1
            while True:
                if (start + j) not in nums_set:
                    if max_k < j:
                        max_k = j
                        break    
                    break            
                j += 1
        
        return max_k
         