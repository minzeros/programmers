# 프로그래머스 - 프린터

def solution(priorities, location):
    answer = 0
    
    while True:
        rank1 = max(priorities) # 가장 높은 우선순위
        cur = priorities.pop(0)
        if cur < rank1:   # 우선순위가 낮은 경우  
            priorities.append(cur)
        else:   # 우선순위가 높은 경우
            answer += 1
            if location == 0:
                return answer

        location -= 1
        if location < 0:
            location = len(priorities)-1



## 다른 풀이1
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer



## 다른 풀이2
def solution(priorities, location):
    answer = 0
    search = sorted(priorities, reverse=True)   # 우선순위대로 정렬
    c = 0
    while True:
        for i, priority in enumerate(priorities):
            # 우선순위가 높은 순서대로 내가 요청한 문서인지 비교
            if priority == search[c]:
                c += 1
                answer += 1
                if i == location:
                    return answer
                    