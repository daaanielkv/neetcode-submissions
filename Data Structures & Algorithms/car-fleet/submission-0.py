class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        res = 1
        inds = [x for (x, _) in sorted(enumerate(position), key=lambda x: x[1])]

        current = 0

        for i in inds[::-1]:
            if not current:
                current = (target - position[i]) / speed[i]
            else:
                t = (target - position[i]) / speed[i]
                if t > current:
                    current = t
                    res += 1
        
        return res