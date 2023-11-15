#16:30 실버2
import sys

n=int(sys.stdin.readline())
inputList=list(map(int,sys.stdin.readline().split()))
dp=[-1001]*(n+1)
for i in range(n):
    if inputList[i]>=0:
        dp[i+1]=max(dp[i]+inputList[i],inputList[i])
    else:
        if dp[i]+inputList[i]>0:
            dp[i+1]=dp[i]+inputList[i]
        else:
            dp[i+1]=inputList[i]

print(max(dp))