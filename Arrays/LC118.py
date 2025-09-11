class Solution(object):
    ans = [[1],[1,1],[1,2,1]]
    def help(self):
        t = 2
        while(t<31):
            temp = []
            i = 0
            while(i<len(self.ans[t])):
                if i==0:
                    temp.append(self.ans[t][i])
                    temp.append(self.ans[t][i]+self.ans[t][i+1])
                elif i==len(self.ans[t])-1:
                    temp.append(self.ans[t][i])
                else:
                    temp.append(self.ans[t][i]+self.ans[t][i+1])
                i+=1
            self.ans.append(temp)
            t+=1
    def generate(self, numRows):
        if len(self.ans)<30:
            self.help()
        return self.ans[:numRows]

