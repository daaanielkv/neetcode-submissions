class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count = {}
        for i in s1:
            count[i] = count.get(i, 0) + 1

        l, r = 0, 0
        current = {}

        while r < len(s2): 

            print(s2[r]) 

            if s2[r] in count:
                current[s2[r]] = current.get(s2[r], 0) + 1
                print(current) 

                while current[s2[r]] > count[s2[r]]:
                    current[s2[l]] -= 1
                    print(current) 
                    l += 1
                
                if current == count:
                    return True

            else:
                current = {}
                l = r + 1

            r += 1

        return False  