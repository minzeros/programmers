# 프로그래머스 - 기능 개발

import math

def solution(progresses, speeds):
    working_days = []
    for prog, sp in zip(progresses, speeds):
        day = math.ceil((100-prog) / sp)
        working_days.append(day)

    answer = []
    front = 0
    for i in range(len(working_days)):
        if working_days[i] > working_days[front]:   # 출시할 기능보다 더 오래 걸리는 기능인 경우
            answer.append(i - front)
            front = i
    answer.append(len(working_days) - front)

    return answer


# Queue의 FIFO을 이용한 다른 풀이
def solution(progresses, speeds):
    answer = []
    time = 1
    count = 0
    
    while len(progresses) > 0:
        if (progresses[0] + time*speeds[0]) >= 100: # 작업 진도가 100을 달성한 경우
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:   # 작업 진도가 100을 달성하지 못한 경우
            if count > 0:   # 해당 기능보다 앞에 있으면서 완성된 기능이 있는 경우
                answer.append(count)
                count = 0
            time += 1

    answer.append(count)
    return answer



# print(solution([93, 30, 55], [1, 30, 5]))
# >>> [2, 1]
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# >>> [1, 3, 2]

