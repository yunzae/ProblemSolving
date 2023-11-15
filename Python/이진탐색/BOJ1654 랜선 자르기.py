import sys

K,N = map(int,sys.stdin.readline().split())
end=0
cableList=[]
for _ in range(K):
    temp=int(sys.stdin.readline())
    cableList.append(temp)
    end+=temp

end = end//N
start=1
midList=[]
while start<=end:
    mid = (start+end)//2
    count=0

    for cable in cableList:
        count+=cable//mid
    if count >=N:
        start=mid+1
    else:
        end=mid-1
    midList.append([mid,count])

result=[]

for i in range(-(len(midList)),0):
    if midList[i][1] >=N:
        result.append(midList[i][0])


print(max(result))


