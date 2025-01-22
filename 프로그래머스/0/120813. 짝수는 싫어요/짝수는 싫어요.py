def solution(n):
    answer = []
    for number in range(n+1):
        if number %2==1:
            answer.append(number)
    return answer