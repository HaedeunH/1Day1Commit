import heapq

def solution(o):
    total=[]
    
    for i in o:
        result=i.split()

        if result[0]=='I':
            heapq.heappush(total,int(result[1]))

        elif total:
            if len(total)>0:
                if result[1]=='1':
                    total.remove(max(total))

                else:
                    heapq.heappop(total)

    if len(total)==0:
        return ([0,0])

    return [max(total),min(total)]

#이게 왜 lv3이지
