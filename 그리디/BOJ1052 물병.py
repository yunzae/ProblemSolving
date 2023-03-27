# 18:50 실버1
from collections import deque
import sys
N,K= map(int,sys.stdin.readline().split())

my_bottle=deque([1 for _ in range(N)])

def solve(bottle):
    new_bottle=deque([])
    while bottle:
        if len(bottle)<2:
            new_bottle.append(bottle.pop())
        else:
            bo1=bottle.popleft()
            bo2=bottle.popleft()
            if bo1==bo2:
                new_bottle.append(bo1+bo2)
            else:
                new_bottle.append(bo1)
                bottle.appendleft(bo2)

    return new_bottle

def solve2(bottle):
    while(len(bottle)>1 and (bottle[-1]==bottle[-2] or bottle[0]==bottle[1])):
        bottle=solve(bottle)
        # print(bottle)

    return bottle


my_bottle= solve2(my_bottle)
count=0
result=-1


while True:
    if len(my_bottle)<=K:
        break
    else:
        count+=my_bottle[-1]
        temp=[1 for _ in range(my_bottle[-1])]
        # print("+++")
        my_bottle+=temp
        my_bottle=solve2(my_bottle)


print(count)
