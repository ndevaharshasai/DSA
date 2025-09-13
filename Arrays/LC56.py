class Solution(object):
    def merge(self, intervals):
        ans = []
        intervals.sort()
        i = 0
        while(i<len(intervals)):
            current = intervals[i]
            start = current[0]
            end = current[1]
            j = i
            while(j<len(intervals) and intervals[j][0]<=end):
                end = max(end,intervals[j][1])
                j+=1
            i=j
            ans.append([start,end])
        return ans
                