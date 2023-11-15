#9:25 실버2

import sys

N=int(sys.stdin.readline())
inputList=list(map(int,sys.stdin.readline().split()))
resultList=[0 for _ in range(N)]

for i in range(N):
    left_p=inputList[i]
    left_count=0
    for j in range(N):
        if resultList[j]==0 and left_count==left_p:
            resultList[j]=i+1
            break
        elif resultList[j]==0:
            left_count+=1


print(*resultList)
