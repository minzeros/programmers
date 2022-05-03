# 프로그래머스 - H-index

def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for h in range(len(citations), 0, -1):
        # h번 이상 인용된 논문이 h개 이상인지 검사
        if citations[h-1] >= h:
            return h
    # 모든 논문이 한번도 인용되지 않은 경우
    return answer



## 다른 풀이1
def solution(citations):
    citations.sort(reverse=True)    # 내림차순으로 정렬
    answer = max(map(min, enumerate(citations, start=1)))
    # start=1 을 설정하므로써 (h번 이상 인용한 논문수, h번) 형태의 리스트가 만들어짐
    # (h번 이상 인용한 논문수, h번) 중에서 min 값 추출
    # min 값들 중에서 가장 큰 max값이 H-index
    return answer