import sys
moneyNum, moneyVal = map(int,sys.stdin.readline().split())

money=[]

for i in range(moneyNum):
    money.append(int(sys.stdin.readline().rstrip()))

money.sort()
dp=[-1]*10001

# 초기값 설정 동전화폐와 값이 일치하는 곳은 1로 처리
for i in money:
    dp[i] = 1

#dp 실행
for i in range(money[0],moneyVal+1):
    temp=[]
    if dp[i]==1:
        continue
    for j in money:
        #인덱스를 벗어나는 것을 방지
        if i<j:
            continue
        #dp[i-j]가 -1 이면 해당 단위 돈으로는 moneyVal을 만들수 없음을 의미, 다음 단위로 넘어감
        if dp[i-j]==-1:
            continue
        temp.append(dp[i-j])

    if len(temp)==0:
        continue
    else:
        dp[i]=min(temp)+1

print(dp[moneyVal])



