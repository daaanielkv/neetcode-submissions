class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        angrms = {}

        for element in strs:

            key = self.make_key(element)
            angrms.setdefault(key, []).append(element)

        return list(angrms.values())
    
    def make_key(self, val):

        key = [0] * 26

        for l in val:
            key[ord(l) - 97] += 1

        return tuple(key)