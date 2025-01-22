def solution(n, k):
    discount = n//10
    answer = n*12000 + k*2000 - discount*2000
    return answer