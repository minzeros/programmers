# 프로그래머스 - 전화번호 목록

# 정확성은 통과, 효율성에서 시간초과 남
def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        n = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:n]:
                return False

    return answer



## 다른 풀이1
import heapq

def solution(phone_book):
    if len(phone_book) == 1:
        return True

    #phone_book.sort(key=lambda x:len(x))
    heapq.heapify(phone_book)
    answer = True
    p_num = heapq.heappop(phone_book)
    while phone_book:
        i = len(p_num)
        # slicing은 범위를 벗어나도 있는 만큼만 출력하므로 no error
        # heap에서 0번째 인덱스의 값은 항상 가장 작은 값
        if p_num == phone_book[0][:i]:
            return False
        p_num = heapq.heappop(phone_book)

    return answer


## 다른 풀이2
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer


## 다른 풀이3
def solution3(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True