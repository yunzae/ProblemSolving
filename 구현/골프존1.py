from collections import deque
def solution(books, target):
    books_deq = deque(books,maxlen=len(books))
    temp=[]
    result=0
    for t in target:
        while books_deq:
            now = books_deq.popleft()
            if t==now:
                while temp:
                    r = temp.pop()
                    books_deq.appendleft(r)
                books_deq.appendleft(t)
                break
            temp.append(now)
            result+=1
    return result