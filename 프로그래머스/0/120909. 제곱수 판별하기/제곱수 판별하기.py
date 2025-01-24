import math
def solution(n):
    k = math.isqrt(n)
    if n%k ==0:
        answer = 1
    else:
        answer = 2
    return answer