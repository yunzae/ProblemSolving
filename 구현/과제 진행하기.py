# 17:42 18:30 37.5점

def solution(plans):
    plans.sort(key=lambda x: x[1])
    for p in plans:
        hour, minute = p[1].split(":")
        start_time = int(hour) * 60 + int(minute)
        p[1] = start_time
        p[2] = int(p[2])

    result = []
    delay = []
    for i in range(len(plans) - 1):
        gap = plans[i + 1][1] - plans[i][1]

        if gap > plans[i][2]:
            result.append(plans[i][0])
            gap -= plans[i][2]

            while gap > 0 and delay:
                assign = delay.pop()
                if gap >= assign[2]:
                    gap -= assign[2]
                    result.append(assign[0])
                else:
                    assign[2] -= gap
                    delay.append(assign)
                    gap = 0

            # for j in range(gap):
            #     assign[2]-=1
            #     if assign[2]==0:
            #         result.append(assign[0])
            #         if not delay:
            #             break
            #         assign = delay.pop()
            #         continue
            #     if j==gap-1:
            #         delay.append(assign)
        elif gap == plans[i][2]:
            result.append(plans[i][0])
        elif gap < plans[i][2]:
            plans[i][2] -= gap
            delay.append(plans[i])

    result.append(plans[-1][0])
    while delay:
        result.append(delay.pop()[0])

    return result
