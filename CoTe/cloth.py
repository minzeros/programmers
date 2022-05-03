# 프로그래머스 - 위장

def solution(clothes):
    hash_map = {}

    # key-value가 (의상종류-의상이름)이 되도록 hash map 생성
    for cloth in clothes:
        if cloth[1] in hash_map:
            hash_map[cloth[1]].append(cloth[0])
        else:
            hash_map[cloth[1]] = [cloth[0]]

    # key별 value 개수를 값으로 갖는 리스트 생성
    array = []
    for v in hash_map.values():
        array.append(len(v) + 1)

    answer = 1
    for v in array:
        answer *= v

    return answer-1


## 다른 풀이1
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:   # key값을 처음 등록할 때 2로 초기화
            clothes_type[t] = 2
        else:   # 이미 등록된 key값인 경우 1 더하기
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1


## 다른 풀이2
from collections import Counter
from functools import reduce
# reduce(집계 함수, 순회 가능한 데이터[, 초기값])

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes]) # 의상 종류별 개수 세기
    # >>> Counter({'headgear': 2, 'eyewear': 1})
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    # x의 초기값 = 1, y는 cnt.values() 데이터값 순회(= [2,1])
    return answer