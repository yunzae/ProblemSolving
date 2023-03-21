#11:11
import sys
import heapq
N,D= map(int,sys.stdin.readline().split())
dist=[i for i in range(D+1)]
graph=[[[1,i+1]] for i in range(D+1)]
graph[D]=[]

for i in range(N):
    start,end,length = map(int,sys.stdin.readline().split())
    if start<=D and end<=D:
        graph[start].append([length,end])


def dijkstra(start):
    hq=[]
    dist[start]=0
    heapq.heappush(hq,(0,start))
    while hq:
        distance,node = heapq.heappop(hq)
        for next_length,next_node in graph[node]:
            if next_length + distance <= dist[next_node]:
                dist[next_node]=next_length+distance
                heapq.heappush(hq,[dist[next_node],next_node])

dijkstra(0)
print(dist[D])