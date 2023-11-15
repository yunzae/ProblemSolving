import sys
import heapq
N,M,C=map(int,sys.stdin.readline().split())
INF=int(1e9)
distance=[INF]*(N+1)

graph=[]
for _ in range(N+1):
    graph.append([])

for i in range(1,M+1):
    temp=list(map(int,sys.stdin.readline().split()))
    graph[temp[0]].append((temp[1],temp[2]))



def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] <dist:
            continue
        for next in graph[now]:
            next_node=next[0]
            next_dist=next[1]+dist
            if distance[next_node]>next_dist:
                distance[next_node]=next_dist
                heapq.heappush(q, (next_dist, next_node))

dijkstra(C)

city_count=0
max_distance=0
for result in distance:
    if result!= INF:
        city_count+=1
        if result>max_distance:
            max_distance=result

print(city_count-1,max_distance)