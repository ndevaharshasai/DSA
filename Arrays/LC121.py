class Solution(object):
    def maxProfit(self, prices):
        ans = 0
        mini = 1e9
        maxi = -1e9
        low = 0
        high = 1
        for i in range(len(prices)):
            if low>high:
                high = low+1
                maxi = prices[high]
            if prices[i]<mini:
                low = i
                mini = prices[i]
            elif prices[i]>=maxi:
                high = i
                maxi = prices[i]
            if low<high:
                ans = max(ans,maxi-mini)
        return ans