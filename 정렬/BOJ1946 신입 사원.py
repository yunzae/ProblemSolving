#9:20 실버1

import sys
T= int(sys.stdin.readline())

def solve():
    rankList=[]

    N=int(sys.stdin.readline())
    for i in range(N):
        rank1,rank2=map(int,sys.stdin.readline().split())
        rankList.append([rank1,rank2,i])
    rankList.sort(key=lambda x: x[0] )
    # print(rankList)

    resultList = []
    resultList.append(rankList[0])
    for i in range(1,N):
        if rankList[i][1]<resultList[-1][1]:
            resultList.append(rankList[i])

    # print(resultList)
    return (len(resultList))



ans=[]
for _ in range(T):
    ans.append(solve())

for a in ans:
    print(a)
