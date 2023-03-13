import sys

M,N= map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))

for i in range(N):
    min_a= min(A)
    max_b= max(B)
    A.remove(min_a)
    A.append(max_b)
    B.remove(max_b)
    B.append(min_a)

print(sum(A))


