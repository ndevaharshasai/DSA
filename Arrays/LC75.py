class Solution(object):
    def sortColors(self, nums):
        i = 0
        for t in range(len(nums)):
            if nums[t]==0:
                nums[i],nums[t] = nums[t],nums[i]
                i+=1
        for t in range(len(nums)):
            if nums[t]==1:
                nums[i],nums[t] = nums[t],nums[i]
                i+=1
        