import sys

direction=[(0,-1),(1,0),(0,1),(-1,0)] #북,동,남,서
mymap = []
n,m=map(int,sys.stdin.readline().split())
x, y, start_direction = map(int,sys.stdin.readline().split())
for i in range(n):
    mymap.append(list(map(int,sys.stdin.readline().split())))
result=0

def move(x,y,d):

    mymap[x][y]= 2 # 지나간
    global result
    result +=1
    for i in range(4):      #네방향 모두 확인
        if mymap[x+direction[(d-1+4)%4][0]][y+direction[(d-1+4)%4][1]]==0:   # d-1 에 +4 해준 이유는 음수가 될 수 있어서 해줌
            x=x+direction[(d-1+4)%4][0]  #x좌표 이동
            y=y+direction[(d-1+4)%4][1]  #y좌표 이동 칸
            d= (d - 1 + 4) % 4          # 방향 변경
            move(x,y,d)                 #이동
        else:
            d=(d-1+4)%4
                            # 함수끝나면서 이전의 함수로 돌아감 = 뒤로 한칸감

move(x,y,start_direction)

print(result)