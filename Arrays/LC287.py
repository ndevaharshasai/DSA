class Solution(object):
    def findDuplicate(self, nums):
        s = set()
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)
        return -1