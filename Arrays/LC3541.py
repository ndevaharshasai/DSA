class Solution(object):
    def maxFreqSum(self, s):
        box = [0]*26
        for i in s:
            box[ord(i)-97]+=1
        vbox = []
        v = [0,4,8,14,20]
        for i in v:
            vbox.append(box[i])
            box[i]=0
        return (max(vbox)+max(box))