class Solution:
    def findRepeatingNumber(self,nums):
        s = set()
        for i in nums:
            if i in s:
                return i 
            else:
                s.add(i)
    def findMissingNumber(self,nums,repeatingNumber):
        n = len(nums)
        i = 1
        while(i<n+1):
            if i not in nums:
                return i 
            i+=1
        return i
    def findMissingRepeatingNumbers(self, nums):
        x = self.findRepeatingNumber(nums)
        y = self.findMissingNumber(nums,x)
        return [x,y]