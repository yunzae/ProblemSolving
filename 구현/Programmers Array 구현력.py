import math


def solution(fees, records):
    answer = []
    carIn = [0 for _ in range(10000)]
    isIn = [False for _ in range(10000)]
    sumTime = [0 for _ in range(10000)]
    for i in range(len(records)):
        inputTime, num, inOut = records[i].split(" ")
        hour, minute = inputTime.split(':')
        time = int(hour) * 60 + int(minute)
        num = int(num)

        if inOut == "IN":
            carIn[num] = time
            isIn[num] = True

        elif inOut == "OUT":
            sumTime[num] += time - carIn[num]
            isIn[num] = False

    for i in range(10000):
        if isIn[i] == True:
            sumTime[i] += (23 * 60 + 59) - carIn[i]

    for i in range(10000):
        if sumTime[i] == 0:
            continue
        else:
            if sumTime[i] <= fees[0]:
                answer.append(fees[1])
            else:
                answer.append(fees[1] + math.ceil(((sumTime[i] - fees[0]) / fees[2])) * fees[3])

    return answer