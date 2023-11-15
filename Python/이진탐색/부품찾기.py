import sys

seller_N = int(sys.stdin.readline().rstrip())
seller = list(map(int,sys.stdin.readline().split()))
customer_N=int(sys.stdin.readline().rstrip())
customer=list(map(int,sys.stdin.readline().split()))
seller.sort()

def search(searchList,target):
    low=0
    high= len(searchList)

    while low<high :
        mid = (high + low) // 2
        if searchList[mid] == target:
            return "yes"
        elif searchList[mid] < target:
            low= mid+1
        else:
            high= mid-1

    return "no"

for i in customer:
    print(search(customer,i),end=" ")







