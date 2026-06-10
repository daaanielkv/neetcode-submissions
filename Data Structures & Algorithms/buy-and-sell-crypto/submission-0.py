class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        m = 0
        mi, ma = prices[0], prices[0]

        for i in prices[1:]:
            
            if i < mi:
                delta = ma - mi
                if delta > m: m = delta
                mi = ma = i
            else:
                ma = i
                delta = ma - mi
                if delta > m: m = delta

        return m