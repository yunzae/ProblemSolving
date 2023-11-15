N,M,K = map(int,input().split())
mylist = list(map(int,input().split()))
mylist.sort()
first= M//K
second = M%K
result = mylist[-1]*first*K + mylist[-2]*second
print(result)
