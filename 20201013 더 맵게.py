import heapq

def solutions(s,k):
    count=0 
    while True:
        scoville=heapq.heapify(s)
        if scoville[0]>k:
            break
        elif len(scoville)==1:
            return -1
        else:
            count+=1
            heapq.heappush(scoville,heapq.heappop(scoville)+(heapq.heappop(scoville)*2))
    return print(count,scoville)

def solution(s,k):
    count=0
    scoville=[]
    for i in s:
        heapq.heappush(scoville,s)
        print(scoville)

    print(scoville,type(scoville))
            


