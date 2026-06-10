class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        vars = tuple(strs[0][:i] for i in range(len(strs[0]) + 1))
        k = len(strs[0])
        i = 1
        while i < len(strs): 
            if k == 0:
                return ''         
            if vars[k] != strs[i][:k]:
                k -= 1
            else:
                i += 1

        return vars[k]