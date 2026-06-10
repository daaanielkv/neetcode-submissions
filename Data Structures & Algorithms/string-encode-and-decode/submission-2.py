class Solution:

    def encode(self, strs: list[str]) -> str:

        return ''.join(f'{len(x)}#{x}' for x in strs)
    
    def decode(self, s: str) -> list[str]:

        print(s)

        res = []
        i = 0

        while i < len(s):
            ind = s.index('#', i)
            lenth = int(s[i:ind])
            res.append(s[ind + 1: ind + 1 + lenth])
            i = ind + 1 + lenth

        return res
