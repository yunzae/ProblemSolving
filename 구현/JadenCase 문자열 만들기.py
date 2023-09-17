# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    s = s.lower()
    s = list(s)
    s[0] = s[0].upper()
    for i in range(len(s)):
        if s[i] == ' ' and i != len(s) - 1:
            s[i + 1] = s[i + 1].upper()

    ans = ''.join(s)
    print(ans)

    return ans