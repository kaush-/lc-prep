class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[-1]
        mx = 0
        n = len(prices) - 1

        for i in range(n, -1, -1):
            if mx < curr - prices[i]:
                mx = curr - prices[i]

            if curr < prices[i]:
                curr = prices[i]

        return mx

