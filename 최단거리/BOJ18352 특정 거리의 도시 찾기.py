import sys
import heapq

N,M,K,X = map(int,sys.stdin.readline().split())
INF=1e9
dist = [INF]*(N+1)
graph=[[] for _ in range(N+1)]
for _ in range(M):
    start_city,end_city= map(int,sys.stdin.readline().split())
    graph[start_city].append(end_city)

def dijkstra(start):
    q=[]
    heapq.heappush(q,[0,start])
    dist[start]=0
    while q:
        distance,node=heapq.heappop(q)
        for next in graph[node]:
            if dist[next]>dist[node]+1:
                dist[next]=dist[node]+1
                heapq.heappush(q,[dist[next],next])


result=[]
dijkstra(X)
for i in range(1,len(dist)):
    if dist[i]==K:
        result.append(i)
if len(result)==0:
    print(-1)
else:
    for r in result:
        print(r)

