from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    count_dic = defaultdict(int)
    mail_dic = defaultdict(set)
    result_dic = defaultdict(int)

    for r in report:
        a, b = r.split(" ")
        count_dic[b] += 1
        mail_dic[b].add(a)

    for id in id_list:
        for m in mail_dic[id]:
            if (count_dic[id] // k) >= 1:
                result_dic[m] += 1

    for id in id_list:
        answer.append(result_dic[id])

    return answer