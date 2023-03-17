import sys

N=int(sys.stdin.readline())

def count(N):
    i = 0
    temp=[1e9]
    while(N>=3):
        if N==3:
            temp.append(i+1)
        if N%5==0:
            temp.append(i+N//5)
        i+=1
        N = N - 3
    return min(temp)


result =count(N)
if result ==1e9:
    print(-1)
else:
    print(result)

