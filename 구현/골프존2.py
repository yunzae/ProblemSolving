from collections import defaultdict

def solution(products, purchased):
    not_purchased=[]
    features = defaultdict(int)
    for product in products:
        temp = product.split(" ")
        if temp[0] in purchased:
            for i in range(1,len(temp)):
                features[temp[i]]+=1
        else:
            not_purchased.append(temp)
    features = sorted(features.items(), key=lambda x: (-x[1],x[0]))

    for f,c in features:
        if len(not_purchased)==1:
            break
        temp=[]
        for n in not_purchased:
            if f in n:
                temp.append(n)
        if len(temp)==0:
            continue
        else:
            not_purchased = temp

    return not_purchased[0][0]

