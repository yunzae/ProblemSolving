# https://school.programmers.co.kr/learn/courses/30/lessons/12928?language=python3

def solution(n):
    answer = 0
    a = []
    for i in range(1,n+1):
        if((n%i)==0):
            a.append(i)
    return sum(a)