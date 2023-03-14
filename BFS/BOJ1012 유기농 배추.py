import sys
from collections import deque
T = int(sys.stdin.readline())
move=[[1,0],[-1,0],[0,1],[0,-1]]

def BFS(start):
    que= deque([start])
    if visited[start[0]][start[1]] == True:
        return 0;

    if myMap[start[0]][start[1]] == 0:
        visited[start[0]][start[1]] = True
        return 0;

    while que:
        q=que.popleft()

        if visited[q[0]][q[1]] == True:
            continue
        visited[q[0]][q[1]] = True
        for m in move:
            nq=[q[0]+m[0],q[1]+m[1]]
            if nq[0] >= M or nq[1] >= N or nq[0] < 0 or nq[1] < 0:
                continue
            if myMap[nq[0]][nq[1]] == 1:
                que.append(nq)
    return 1;


for _ in range(T):
    M,N,K = map(int,sys.stdin.readline().split())
    myMap=[[0 for _ in range(N)]for _ in range(M)]
    visited=[[False for _ in range(N)]for _ in range(M)]
    for i in range(K):
        temp=list(map(int,sys.stdin.readline().split()))
        myMap[temp[0]][temp[1]] = 1
    result=0
    for i in range(M):
        for j in range(N):
            result+=BFS([i,j])

    print(result)

