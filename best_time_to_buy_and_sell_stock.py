# straightforward, keep track of new lows and check to see
# if leg from new low supercedes the max profit from the previous low

def maxProfit(self, prices: List[int]) -> int:
    cmin = prices[0]
    cmax = 0
    for i in range(1, len(prices)):
        if prices[i] < cmin:
            cmin = prices[i]
        else:
            cmax = max(prices[i] - cmin, cmax)
    return cmax
