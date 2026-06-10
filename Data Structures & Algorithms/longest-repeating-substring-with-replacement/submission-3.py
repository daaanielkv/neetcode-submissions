class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        N = 1
        freq = {s[l]: 1}

        for r in range(1, len(s)):

            freq[s[r]] = freq.get(s[r], 0) + 1

            if (r - l + 1) - max(freq.values()) <= k:
                N = max(N, r - l + 1)
            else:
                freq[s[l]] -= 1
                l += 1

        return N
            