ls = list(map(int,input().split()))
for _ in range(len(ls)):
    i = 0
    while(i<len(ls)-1):
        if ls[i]>=ls[i+1]:
            ls[i],ls[i+1] = ls[i+1],ls[i]
        i+=1
print(ls)