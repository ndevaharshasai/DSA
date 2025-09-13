class Solution(object):
    def nextPermutation(self, nums):
        numss = [i for i in nums]
        numss.sort(reverse=True)
        if nums == numss:
            nums.sort()
            return
        j = len(nums)-1
        i = j-1
        while(i>0 and nums[i]>=nums[j]):
            i-=1
            j-=1
        temp = nums[i]
        m = 1e9
        t = i+1
        tl = i+1
        while(t<len(nums)):
            if nums[t]<=m and nums[t]>temp:
                tl = t
                m = nums[t]
            t+=1
        nums[i],nums[tl] = nums[tl],nums[i]
        x = nums[i+1:]
        x.sort()
        numss = nums[:i+1]
        print(numss)
        while(len(nums)>0):
            nums.pop(0)
        for i in numss:
            nums.append(i)
        for i in x:
            nums.append(i)