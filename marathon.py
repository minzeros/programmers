# 프로그래머스 - 완주하지 못한 선수

def solution(participant, completion):
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()


# 다른 풀이
# Counter 객체 사용
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# 다른 풀이
# hash 함수 사용
def hash_solution(participant, completion):
    answer = ''
    temp = 0
    dict = {}
    for part in participant:
        dict[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dict[temp]

    return answer

part = ["marina", "josipa", "nikola", "vinko", "filipa"]
com = ["josipa", "filipa", "marina", "nikola"]

hash_solution(part, com)