import heapq

def solution(s,k):
    count=0
    scoville=[]
    for i in s:
        heapq.heappush(scoville,i)
    while(True):
        if scoville[0]>=k:
            break
        elif len(scoville)==1:
            return -1
        else:
            count+=1
            heapq.heappush(scoville,heapq.heappop(scoville)+(heapq.heappop(scoville)*2))
            return count
            
#append나 min pop 대신 힙을 이용하면 효율성이 좋다는점

            


