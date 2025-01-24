def solution(money):
    jan = money//5500
    don = money-5500*jan
    answer = [jan, don]
    return answer