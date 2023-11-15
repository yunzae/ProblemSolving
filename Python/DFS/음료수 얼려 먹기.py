import sys
myMap=[]
move=[(-1,0),(1,0),(0,1),(0,-1)]

N,M= map(int,sys.stdin.readline().split())

visited=[[True]*N for _ in range(M)]

for i in range(M):
    temp = (sys.stdin.readline().split())
    myMap.append(list(map(int,temp[0])))


def search(start_x,start_y):
    if start_x >= M or start_y >= N or start_x < 0 or start_y < 0:
        return 0
    if visited[start_x][start_y]==True and myMap[start_x][start_y]==0:
        visited[start_x][start_y]=False
        for i in move:
            next_x = start_x+i[0]
            next_y = start_y+i[1]
            search(next_x,next_y)
        return 1
    else:
        return 0


count=0
for i in range(M):
    for j in range(N):
        count +=  search(i,j)
print(count)