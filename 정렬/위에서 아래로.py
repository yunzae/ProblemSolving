import sys

N = int(sys.stdin.readline())
numbers=[]

for i in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort(reverse=True)
print(numbers)