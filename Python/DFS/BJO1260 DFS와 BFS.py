import sys
from collections import deque
N,M,V = map(int, sys.stdin.readline().split())
myMap = []
for i in range(M):
    temp= list(map(int,sys.stdin.readline().split()))
    myMap.append([temp[0],temp[1]])
    myMap.append([temp[1],temp[0]])

myMap.sort(key= lambda x:x[1])
visited=[False]*(N+1)
DfsResult=[]
BfsResult=[]

def DFS(start):
    if visited[start] == True:
        return 0;
    visited[start]=True
    DfsResult.append(start)
    for temp in myMap:
        if temp[0] == start:
            DFS(temp[1])
def BFS(start):
    que = deque([start])
    while que:
        nq = que.popleft()
        if visited[nq] == True:
            continue
        visited[nq]=True
        BfsResult.append(nq)
        for temp in myMap:
            if temp[0] == nq:
                que.append(temp[1])
DFS(V)
visited=[False]*(N+1)
BFS(V)
print(*DfsResult)
print(*BfsResult)


