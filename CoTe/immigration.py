# 프로그래머스 - 입국심사
# 이진탐색 사용

def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n

    while start < end:
        mid = (start + end) // 2
        people = 0
        for time in times:
            people += mid // time

        if people >= n:
            end = mid
        else:
            start = mid + 1

    answer = start
    return answer

print(solution(6, [7, 10]))