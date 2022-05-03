# 프로그래머스 - 주식가격

def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        time = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:  # 주식 가격이 떨어지지 않는 동안 time 증가
                time += 1
            else:   # 주식 가격이 떨어지면 for문 탈출
                time += 1
                break
        answer.append(time)
    answer.append(0)
    return answer



## 다른 풀이1
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer



## 다른 풀이2 -> 가장 속도 빠름!
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)  # 큐 사용
    while prices:
        c = prices.popleft()    # 맨 앞에 있는 주식 가격
        count = 0
        for i in prices:
            if c > i:   # 주식 가격이 떨어지면 for문 탈출
                count += 1
                break
            # 주식 가격이 떨어지지 않는 동안 count 증가
            count += 1
        answer.append(count)

    return answer