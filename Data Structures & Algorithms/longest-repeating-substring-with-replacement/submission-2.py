class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        N = 1
        freq = {}
        max_freq = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])  # O(1)

            if (r - l + 1) - max_freq <= k:
                N = max(N, r - l + 1)
            else:
                freq[s[l]] -= 1
                l += 1

        return N