#https://school.programmers.co.kr/learn/courses/30/lessons/12931
def solution(n):
    answer = 0
    s = str(n)
    ans=0
    for i in range(len(s)):
        ans += int(s[i])

    return ans