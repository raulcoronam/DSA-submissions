class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        compra, venta, maxProfit = 0, 1, 0

        while venta < len(prices): 
            if prices[compra] < prices[venta]: 
                profit = prices[venta] - prices[compra]
                maxProfit = max(maxProfit, profit)
            else: 
                compra = venta
            venta += 1
        return maxProfit