import collections


def solution(gems):
    gemNum = len(set(gems))
    lt = 0
    rt = 0
    selected = collections.defaultdict(int)
    answer = [0, 1e9]
    selected[gems[lt]] += 1
    while True:
        if len(selected) < gemNum:
            if rt == len(gems) - 1:
                break
            else:
                rt += 1
                selected[gems[rt]] += 1
        else:
            if rt - lt + 1 < answer[1] - answer[0] + 1:
                answer = [lt + 1, rt + 1]
            if rt - lt + 1 == answer[1] - answer[0] + 1 and lt < answer[0]:
                answer = [lt + 1, rt + 1]

            selected[gems[lt]] -= 1
            if selected[gems[lt]] <= 0:
                selected.pop(gems[lt], None)
            lt += 1

    return answer