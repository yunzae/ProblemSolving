# 11:16 12:00 테케8번틀림 97.1점

def solution(picks, minerals):
    fatigue = []

    dia = 0
    iron = 0
    stone = 0
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            dia += 1
        if minerals[i] == "iron":
            iron += 1
        if minerals[i] == "stone":
            stone += 1
        if dia + iron + stone == 5 or i == len(minerals) - 1:
            dia_fatigue = dia + iron + stone
            iron_fatigue = dia * 5 + iron + stone
            stone_fatigue = dia * 25 + iron * 5 + stone
            fatigue.append([dia_fatigue, iron_fatigue, stone_fatigue])
            dia = 0
            iron = 0
            stone = 0
    # 스톤, 철, 다이아가 많은 순으로 정렬
    print(fatigue)
    fatigue = fatigue[:sum(picks)]
    fatigue.sort(key=lambda x: (x[2], x[1], x[0]))
    sum_fatigue = 0

    i = 0
    print(fatigue)
    while fatigue:
        i += 1
        if i <= picks[0]:
            sum_fatigue += fatigue[-1][0]
            fatigue.pop()
        elif i <= picks[0] + picks[1]:
            sum_fatigue += fatigue[-1][1]
            fatigue.pop()
        elif i <= picks[0] + picks[1] + picks[2]:
            sum_fatigue += fatigue[-1][2]
            fatigue.pop()
        else:
            break
    print(fatigue)
    return sum_fatigue