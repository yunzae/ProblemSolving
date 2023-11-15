import sys

N = int(sys.stdin.readline())
mylist=[]
result=[]
for i in range(N):
    temp=list(sys.stdin.readline().split())
    mylist.append((int(temp[1]),temp[0]))

mylist.sort()

for i in mylist:
    result.append(i[1])

print(result)
# [[30,a],[20,b]]