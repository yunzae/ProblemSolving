#08:48 실버1 90분 실패
import sys
from collections import deque
string = sys.stdin.readline().rstrip()




print(string)
def solve(string):
    first=[]
    for i in range(len(string)-1):
        if string[i]=='(' and string[i+1]==')':
            first.append(2)
        elif string[i] =='[' and string[i+1]==']':
            first.append(3)
        else:
            first.append(string[i])
        if first[-1]==2 or first[-1]==3:
            continue
        else:
             first.append(string[i+1])
    second=[]
    print(*first)
    k=0
    while k<5:
        string
        #괄호의 짝이 없으면 리턴0
        #숫자가 있다면 그 양쪽 괄호 확인해서 계산
        #숫자끼리 붙어 있다면 더하기
        for i in range(len(first)):
            if type(first[i])==type(1):
                if i-1>0 and i+1<len(first)-1:
                    if first[i-1]=='(' and first[i+1]==')':
                        second.pop()
                        second.append(int(2*first[i]))
                    elif first[i - 1] == '[' and first[i + 1] == ']':
                        second.pop()
                        second.append(int(3 * first[i]))
                    else:
                        second.append(first[i])
                else:
                    second.append(first[i])

            else:
                if i!=0 and type(first[i-1])==type(1):
                    pass
                else:
                    second.append(first[i])
        k+=1

        first=second[:]
        print(*second)
        second=[]




    return first

# 괄호의 짝이 있는지 체크 함수

print(solve(string))