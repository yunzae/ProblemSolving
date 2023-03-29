#16:07 실버1 35분
import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
visited = [False]*(N+1)

for i in range(M):
    temp1,temp2= map(int,sys.stdin.readline().split())
    if temp2 not in graph[temp1]:
        graph[temp1].append(temp2)
    if temp1 not in graph[temp2]:
        graph[temp2].append(temp1)


def bfs(start):
    visited = [False] * (N + 1)
    deq= deque([[start,0]])
    bacon=0
    while(deq):
        temp=deq.popleft()
        q=temp[0]
        depth=temp[1]
        if visited[q] == True:
            continue
        bacon += depth
        depth+=1
        visited[q]=True
        for g in graph[q]:
            deq.append([g,depth])
    return bacon

result=[]

for i in range(1,N+1):
    result.append([bfs(i),i])

result.sort(key= lambda x:(x[0],x[1]))

print(result[0][1])