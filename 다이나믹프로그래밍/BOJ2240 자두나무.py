import sys
T,W =map(int,sys.stdin.readline().split())
plum=[]
for i in range(T):
    plum.append(int(sys.stdin.readline()))

DP=[[0 for _ in range(W+1)] for _ in range(T+1)]

for i in range(T):
    for k in range(W+1):
        if plum[i]==1:
            if k==0:
                DP[i+1][k] = DP[i][k]+1
            elif k%2==0:
                DP[i+1][k] = max(DP[i][k]+1,DP[i][k-1]+1)
            else:
                DP[i+1][k] = max(DP[i][k],DP[i][k-1])
        else:
            if k==0:
                DP[i+1][k] = DP[i][k]
            elif k%2==0:
                DP[i+1][k]=max(DP[i][k],DP[i][k-1])
            else:
                DP[i+1][k] =max(DP[i][k]+1, DP[i][k-1]+1)

print(max(DP[-1]))