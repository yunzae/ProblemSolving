# 15:05 level3 16:30

def solution(n, t, m, timetable):
    from collections import deque
    new_timetable = []
    for i in range(len(timetable)):
        temp = int(timetable[i][0:2] + timetable[i][3:5])
        new_timetable.append(temp)
    new_timetable.sort()
    new_timetable = deque(new_timetable)
    buslist = [[] for _ in range(n)]
    bustime = 900

    for i in range(n):
        next_bustime = 0
        buslist[i].append(bustime)
        if int(str(next_bustime)[-2:]) + t >= 60:
            next_bustime = bustime + t + 100 - 60
        else:
            next_bustime = bustime + t

        while new_timetable:
            if len(buslist[i]) >= m + 1:
                break
            q = new_timetable.popleft()
            if q <= bustime:
                buslist[i].append(q)
            else:
                new_timetable.appendleft(q)
                break

        bustime = next_bustime

    ans = ""
    lastbus = buslist[-1][1:]
    lastbus.sort()

    # 자리가 남았으면 버스출발시간이 답
    if len(buslist[-1]) < m + 1:
        ans = str(buslist[-1][0])

    # 자리가 없으면 승객중 제일 늦는사람 보다 1분빠르게, 시간이 같은경우도 생각해야함
    else:
        for i in range(1, len(lastbus) + 1):
            if len(str(lastbus[-i])) > 2:
                if i == len(lastbus):
                    if int(str(lastbus[-i])[-2:]) == 0:
                        if len(str(lastbus[-i])) == 4 and int(str(lastbus[-i])[0:2]) > 10:
                            hour = str(int(str(lastbus[-i])[0:2]) - 1)
                            min = str(59)
                            ans = hour + min
                        else:
                            hour = "0" + str(int(str(lastbus[-i])[0]) - 1)
                            min = str(59)
                            ans = hour + min


                    else:
                        if len(str(lastbus[-i])) == 4 and int(str(lastbus[-i])[0:2]) > 10:
                            hour = str(lastbus[-i])[0:2]
                            min = str(lastbus[-i])[1] + str(int(str(lastbus[-i])[2]) - 1)
                            ans = hour + min
                        else:
                            hour = "0" + str(lastbus[-i])[0]
                            min = str(lastbus[-i])[1] + str(int(str(lastbus[-i])[2]) - 1)
                            ans = hour + min

                else:
                    if lastbus[-i] == lastbus[-(i + 1)]:
                        continue
                    else:
                        if int(str(lastbus[-i])[-2:]) == 0:
                            if len(str(lastbus[-i])) == 4 and int(str(lastbus[-i])[0:2]) > 10:
                                hour = str(int(str(lastbus[-i])[0:2]) - 1)
                                min = str(59)
                                ans = hour + min
                            else:
                                hour = "0" + str(int(str(lastbus[-i])[0]) - 1)
                                min = str(59)
                                ans = hour + min

                        else:
                            if len(str(lastbus[-i])) == 4 and int(str(lastbus[-i])[0:2]) > 10:
                                hour = str(lastbus[-i])[0:2]
                                min = str(lastbus[-i])[-2] + str(int(str(lastbus[-i])[-1]) - 1)
                                ans = hour + min
                            else:
                                hour = "0" + str(lastbus[-i])[0]
                                min = str(lastbus[-i])[-2] + str(int(str(lastbus[-i])[-1]) - 1)
                                ans = hour + min

                    break

    if len(ans) == 4:
        answer = ans[:2] + ":" + ans[2:]
    elif len(ans) == 3:
        answer = ans[:1] + ":" + ans[1:]
    else:
        answer = "00:" + ans
    return lastbus, ans