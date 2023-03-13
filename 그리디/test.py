from queue import PriorityQueue
que = PriorityQueue()
# que = PriorityQueue(maxsize=8) 디폴트사이즈는 무한대이다. 크기설정이 왼쪽과 같이하면 된다.

# 아래처럼 입력하면 오름차순으로 정렬이 된다.
que.put(4) # 원소추가
que.put(1)
que.put(7)
que.put(3)

#정렬기준을 바꾸고 싶다면 아래처럼 하면된다.
# (우선순위, 값)의 형태로 저장할 수도 있음
que.put((3, 'Apple'))
que.put((1, 'Banana'))
que.put((2, 'Cherry'))

que.get()  # 1
que.get()[1]  # (우선순위, 값)의 형태에서 값 반환

print(que.get()[1])  # Banana
print(que.get()[1])  # Cherry
print(que.get()[1])  # Apple