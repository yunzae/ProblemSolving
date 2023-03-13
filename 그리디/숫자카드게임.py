N,M = map(int,input().split())
mylist=[]
for i in range(N):
    temp=list(map(int,input().split()))
    temp.sort()
    mylist.append(temp[0])

mylist.sort()
print(mylist[-1])
