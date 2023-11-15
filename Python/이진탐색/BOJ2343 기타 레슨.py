# 9:55 실버1

import sys

N,M =map(int,sys.stdin.readline().split())
bluelay_list=list(map(int,sys.stdin.readline().split()))

def greedy(time,video_list):
    sum=0
    count=1
    for video in video_list:
        if video+sum <=time:
            sum+=video
        else:
            sum=video
            count+=1
    return(count)

def bineary():
    start=max(bluelay_list)
    end=sum(bluelay_list)
    time=end
    while start<=end:
        mid=(start+end)//2
        need_disk= greedy(mid, bluelay_list)
        # print("start: ", start,"end: ", end,"mid: ",mid,"need: ",need_disk)

        if mid<time:
            if need_disk<=M:
                time = mid
                end = mid - 1
            else:
                start=mid+1
        else:
            start=mid+1

    return time
print(bineary())

