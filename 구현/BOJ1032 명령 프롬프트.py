
import sys

N= int(sys.stdin.readline())
inputList=[]
for i in range(N):
    inputList.append(str(sys.stdin.readline().rstrip()))

result=""

for i in range(len(inputList[0])):
    count=1
    for j in range(N-1):
        if inputList[j][i]==inputList[j+1][i]:
            count+=1
    if count == N:
        result+=inputList[0][i]
    else:
        result+='?'


print(result)
