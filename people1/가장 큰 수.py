def solution(n):
    num=list(map(str,n))
    num.sort(key=lambda x:x*3,reverse=True)
    
    return str(int("".join(num)))