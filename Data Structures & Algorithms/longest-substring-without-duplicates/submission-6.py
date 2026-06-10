class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        m = 0
        l = 0
        current = set()

        for r in range(len(s)):
            
            while s[r] in current:
                current.remove(s[l])
                l += 1
                
            current.add(s[r])

            m = max(m, r - l + 1)

        return m