import json

stone = [1, 2, 1, 4]
dog = [{
    "name" : "루비독",
    "age" : "95년생",
    "jump" : "3",
    "weight" : "4",
    },{
    "name" : "피치독",
    "age" : "95년생",
    "jump" : "3",
    "weight" : "3",
    },{
    "name" : "씨-독",
    "age" : "72년생",
    "jump" : "2",
    "weight" : "1",
    },{
    "name" : "코볼독",
    "age" : "59년생",
    "jump" : "1",
    "weight" : "1",
    }]

def bridge(stone,dog):
  answer=[i['name'] for i in dog] #결과값 출력할 리스트 만들기
  
  for i in dog: # 개 한마리씩 돌다리 가야하니까 
    location=0 #돌의위치 값 만들기
    while location<len(stone)-1: #돌다리 건너는데 다리를 다 건너야 하는 조건
      location += int(i['jump']) # 개의위치는 점프한만큼 이동하니까
      stone[location-1]-=int(i['weight']) # 그리고 돌의무게는 개의 무게이상으로 감당해야해서
      if stone[location-1]<0:
        del answer[answer.index(i['name'])]
        break
  return answer

print(bridge(stone.copy(),dog.copy()))

JSONdog=json.dumps(dog,ensure_ascii=False)
#ensure_ascii=False >> json으로 저장시 유니코드 문자열로 표시하는 것

JSONdog=json.loads(JSONdog)
JSONdog[0]

#실제업무에서는 JSON으로 데이터를 부르고 처리할 일이 많다. 

#참조하는 형태가 아닌 값을 복사하는 형태로 값을 가져오려면 copy모듈을 사용하면 된다.
#지역변수에서 밖에 있는 값을 원래 건들수 없는데 리스트는 주소를 복사해서 받으니까 수정이 가능하다. 그래서 리스트처럼 값을 복사하는 형태로 가져오기 위해서는 copy모듈을 사용한다. 

#remove o(N)
#del o(1) 
# 고로 del을 쓰는걸 권장한다. 