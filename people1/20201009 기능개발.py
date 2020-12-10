from collections import Counter
import math

def solution(progresses, speeds):
    
    for i in range(len(progresses)):
        progresses[i]=math.ceil((100-progresses[i])/speeds[i])


    for i in range(1,len(progresses)):
        if progresses[i-1]>progresses[i]:
            progresses[i]=progresses[i-1]

    c=Counter(progresses)
    values=c.values()

    return list(values)









