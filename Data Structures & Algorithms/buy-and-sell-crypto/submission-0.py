class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy=prices[0]
        maxp=0

        for sell in prices:
            maxp=max(maxp,sell-minbuy)
            minbuy=min(sell,minbuy)
        return maxp     