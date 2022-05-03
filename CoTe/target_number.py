# 프로그래머스 - 타겟넘버

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((numbers[0],0))
    queue.append((numbers[0] * -1, 0))
    n = len(numbers)
    
    while queue:
        num, cnt = queue.popleft()
        cnt += 1
        if cnt < n: # numbers를 모두 사용하기 전인 경우
            # (다음 인덱스의 number를 더하거나 뺀 결과값, 사용한 number 개수)를 큐에 삽입
            queue.append((num + numbers[cnt], cnt))
            queue.append((num - numbers[cnt], cnt))
        else:   # numbers를 모두 사용한 경우
            if num == target:
                answer += 1     
    return answer



## 다른 풀이1
def solution(numbers, target):
    q = [0]
    for n in numbers:
        s = []
        for _ in range(len(q)):
            x = q.pop()
            s.append(x + n)
            s.append(x + n*(-1))
        q = s.copy()
    return q.count(target)



## 다른 풀이2
def solution(numbers, target):
    if not numbers and target == 0: # numbers에 값이 없고, target이 0인 경우
        return 1
    elif not numbers:   # numbers에 값이 없고, target이 0이 아닌 경우
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])