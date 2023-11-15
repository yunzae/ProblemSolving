import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
myMap = []
visited=[[False]*M for _ in range(N)]
moves = [[1,0],[0,1],[-1,0],[0,-1]]
for i in range(N):
    temp=list(map(int,sys.stdin.readline().split()[0]))
    myMap.append(temp)

def BFS(start,end):
    que= deque()
    que.append(start)
    while que:
        q=que.popleft()
        if q[0] == end[0] and q[1] == end[1]:
            return myMap[end[0]][end[1]]
        visited[q[0]][q[1]] = True
        for move in moves:
            nq_x=q[0]+move[0]
            nq_y=q[1]+move[1]
            if nq_x < 0 or nq_y< 0 or nq_x > end[0] or nq_y > end[1]:
                continue
            if myMap[nq_x][nq_y] == 0 or visited[nq_x][nq_y] == True:
                continue
            if myMap[nq_x][nq_y] == 1:
                myMap[nq_x][nq_y] = myMap[q[0]][q[1]] + 1
            que.append([nq_x,nq_y])
    return "No way"


print(BFS([0,0],[N-1,M-1]))
#print(myMap)
#print(visited)

for i in myMap:
    print(i)





