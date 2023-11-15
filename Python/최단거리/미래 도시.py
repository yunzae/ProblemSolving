import sys
INF = int(1e9)
companyNum,wayNum = map(int,sys.stdin.readline().split())
myMap= [[INF]*(companyNum+1) for _  in range(companyNum+1)]

for i in range(1,companyNum+1):
    myMap[i][i]=0

for _ in range(wayNum):
    temp=list(map(int,sys.stdin.readline().split()))
    myMap[temp[0]][temp[1]] = 1
    myMap[temp[1]][temp[0]] = 1

X ,K = map(int,sys.stdin.readline().split())


for i in range(1,companyNum+1):
    for j in range(1,companyNum+1):
        for k in range(1,companyNum+1):
            myMap[i][j] = min(myMap[i][j], myMap[i][k] + myMap[k][j])


result= myMap[1][K]+myMap[K][X]

if result>=INF:
    print(-1)
else:
    print(result)