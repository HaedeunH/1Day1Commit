import collections

list=[['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
a=[]
for x,y in list:
    a.append(y)
    print(a)

total=collections.Counter(a)


# a리스트에 list[][i]의 종류를 모아둠
#이걸 카운트해서 딕셔너리 형식으로 만들어
#value값을 이용하든 아님 리스트에 [2,1]의 값을 만들든 해서
#해당 리스트[i]+1 해버리고
#리스트 내 값들을 다 더해버리고 -1 한걸 리턴하기 
