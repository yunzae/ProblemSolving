#20:05 level2
from collections import deque
def solution(cacheSize, cities):
    time=0
    cache=deque({})
    cities_deq=deque(cities)
    while cities_deq:
        city = cities_deq.popleft()
        city=city.lower()
        if city in cache:
            time+=1
            c=cache.remove(city)
            cache.append(city)

        else:
            time+=5
            if len(cache)<cacheSize:
                cache.append(city)
            elif cacheSize==0:
                pass
            else:
                cache.popleft()
                cache.append(city)


    return time