import sys

N=int(sys.stdin.readline().rstrip())
dp=[0]*(N+1)

dp[1]=0
dp[2]=1

for i in range(2,N+1):
    temp = [N] * 4
    if i%5 == 0:
        temp[0] = dp[i//5] + 1
    if i%3 == 0:
        temp[1] = dp[i//3] + 1
    if i%2 == 0:
        temp[2] = dp[i//2] + 1
    temp[3]=dp[i-1]+1
    dp[i]=min(temp)

print(dp)
print(dp[N])