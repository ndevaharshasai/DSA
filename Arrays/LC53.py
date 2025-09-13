class Solution(object):
    def maxSubArray(self, nums):
        maxi = -1e9
        s = 0
        for current in nums:
            s+=current
            if s<=current:
                s = current
            maxi = max(s,maxi)
        return maxi