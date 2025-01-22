def solution(n):
    answer=0
    for number in range (n+1):
        if number%2==0:
            answer+=number
    return answer