#10:35 골드5 45분,hint(시간초과)

import sys
import heapq
INF=1e9
N = int(sys.stdin.readline())
M= int(sys.stdin.readline())
graph=[[]for _ in range(N+1)]
dist=[INF]*(N+1)
dist[0] = 0
for i in range(M):
    start,end,cost=map(int,sys.stdin.readline().split())
    graph[start].append([end,cost])
    graph[end].append([end,cost])

start,end = map(int,sys.stdin.readline().split())

def daijkstra(start):
    hq=[]
    dist[start]=0
    heapq.heappush(hq,[0,start])
    while hq:
        distance,node=heapq.heappop(hq)
        if dist[node] < distance:
            continue
        for next_node,next_cost in graph[node]:
            if dist[next_node] <next_cost:
                continue
            if dist[next_node] > distance+next_cost:
                dist[next_node] = distance+next_cost
                heapq.heappush(hq,[distance+next_cost,next_node])

daijkstra(start)
print(dist[end])


