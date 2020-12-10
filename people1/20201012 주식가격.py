prices=[1,2,3,2,3]
total=[0]*len(prices)

for i in range(len(prices)-1):
    for j in range(len(prices)-1):
        if prices[i]<prices[j]:
            break
        else:
            total[j]+=1
            
print(total)

#기능개발도 그렇고 어렵게 생각하지 않으면 쉽게 풀 수 있는 문제.
#문제를 잘 이해하지 못해 이해하는데 조금 시간이 걸렸다.
#풀다가 잠깐 다른분 접근법보고 힌트를 얻어 푸니까 허탈함. 
