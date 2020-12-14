from collections import Counter
import math

def solution(p,s):

    
    for i in range(len(p)):
        p[i]=math.ceil((100-p[i])/s[i])

    for j in range(1,len(p)):
        if(p[j-1]>p[j]):
            p[j]=p[j-1]

    a=Counter(p)
    val=a.values()
    return list(val)