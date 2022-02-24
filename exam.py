# 프로그래머스 - 모의고사

def solution(answers):
    # 세 명의 학생이 답을 찍는 패턴 정의
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]

    # 각 패턴의 길이
    p1 = len(pattern1)
    p2 = len(pattern2)
    p3 = len(pattern3)

    # 세 학생의 정답 개수를 저장할 리스트
    scores = [0,0,0]
    # enumerate() 사용해서 답 패턴 반복
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % p1]:
            scores[0] += 1
        if answer == pattern2[idx % p2]:
            scores[1] += 1
        if answer == pattern3[idx % p3]:
            scores[2] += 1

    # 문제를 제일 많이 맞춘 학생을 저장할 리스트
    result = []
    for idx, sc in enumerate(scores):
        if sc == max(scores):
            result.append(idx+1)

    return result


print(solution([1,3,2,4,2]))
# >>> [1,2,3]
print(solution([1,2,3,4,5]))
# >>> [1]