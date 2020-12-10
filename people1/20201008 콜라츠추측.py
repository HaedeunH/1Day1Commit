'''
콜라츠 추측
https://programmers.co.kr/learn/courses/30/lessons/12943
'''

def solution(num):
    
    count=0
    
    while num != 1:

        if num % 2 == 0:
            num=num//2
            count+=1
        elif num % 2 != 0:
            num=num*3+1
            count+=1

        if count >= 500:
            count=-1
            break
        
    answer=count
    return answer
