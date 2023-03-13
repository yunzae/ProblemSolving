import sys
N,M=map(int,sys.stdin.readline().split())
ricecakeList=list(map(int,sys.stdin.readline().split()))
ricecakeList.sort()

def search(ricecakeList,mine):
    low=min(ricecakeList)
    high= max(ricecakeList)
    result = high
    while low<high:
        mid = (low + high) // 2
        cut_result = 0
        for i in ricecakeList:
            if mid < i:
                cut_result+=(i-mid)

        if cut_result == mine:
            return mid

        elif cut_result < mine:
            high=mid-1

        else:           #cut_result > mine:
            low=mid+1
            # if mid < result:  조건문이 필요없다. 조금씩 자를 떡을 늘려가기에 마지막에 자르는 떡이 가장 작다.
            result = mid

    return result

print(search(ricecakeList,M))