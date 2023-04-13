# 16:55 level2 50분만에 푼건 84.6점


def solution(str1, str2):
    Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    strList1 = []
    strList2 = []
    for i in range(len(str1) - 1):
        if str1[i].upper() in Alphabet and str1[i + 1].upper() in Alphabet:
            strList1.append(str1[i].upper() + str1[i + 1].upper())
    for i in range(len(str2) - 1):
        if str2[i].upper() in Alphabet and str2[i + 1].upper() in Alphabet:
            strList2.append(str2[i].upper() + str2[i + 1].upper())

    gyoList = list(set(strList1) & set(strList2))
    hapList = list(set(strList1) | set(strList2))

    gyo = 0
    hap = 0
    for i in range(len(gyoList)):
        gyo += min(strList1.count(gyoList[i]), strList2.count(gyoList[i]))
    for i in range(len(hapList)):
        hap += max(strList1.count(hapList[i]), strList2.count(hapList[i]))

    if hap == 0:
        ans = 1 * 65536

    else:
        ans = int(gyo / hap * 65536)
    return ans