# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    s = list(map(int,list(s.split())))
    print(s)
    a = []
    a.append(min(s))
    a.append(max(s))
    print(*a)
    ans = str(a[0])+" "+str(a[1])
    return ans