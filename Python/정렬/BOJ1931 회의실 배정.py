
import sys

N = int(sys.stdin.readline())
inputMeetingList=[]
temp=[]
meetingList=[]
for i in range(N):
    inputMeetingList.append(list(map(int,sys.stdin.readline().split())))

inputMeetingList.sort(key= lambda x:(x[1],x[0]))

end = 0
count = 0
for meet in inputMeetingList:
    if meet[0] >= end:
        count += 1
        end = meet[1]
print(count)

