import collections

def solution(clothes):
    a=[]
    b=[]
    result=1

    for x,y in clothes: 
        a.append(y)

    total=collections.Counter(a)
    color=total.values()

    for i in color: 
        b.append(i)

    for i in range(len(b)):
        result*=(b[i]+1)
    return result-1
