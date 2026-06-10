class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        frq = {}
        batches = [[] for _ in range(len(nums) + 1)] 
        most = []
        
        for n in nums:
            frq[n] = frq.get(n, 0) + 1
        
        for key, v in frq.items():
            batches[v].append(key)

        count = 0

        for batch in batches[::-1]:
            for num in batch:
                most.append(num)
                if len(most) == k:
                    return most 

        return most