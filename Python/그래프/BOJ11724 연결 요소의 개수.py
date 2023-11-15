# 20:20
import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
graph=[[]for _ in range(N+1)]
visited=[False for _ in range(N+1)]

for _ in range(M):
    node1,node2 = map(int,sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def bfs(start):

    if visited[start]==True:
        return 0
    deq = deque([start])

    while(deq):
        q= deq.popleft()
        if visited[q] == True:
            continue
        visited[q]=True
        for g in graph[q]:
            deq.append(g)
    return 1


count=0
for i in range(1,N+1):
    count+=bfs(i)
print(count)
