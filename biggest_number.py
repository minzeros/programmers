# 프로그래머스 가장 큰 수

def solution(numbers):
  numbers = list(map(str, numbers))
  numbers.sort(key=lambda x:x*3, reverse=True)
  answer = str(int(''.join(numbers)))
  return answer

# 다른 방법
import functools

def solution2(numbers):
  numbers = list(map(str, numbers))
  numbers.sort(key=functools.cmp_to_key(comparator), reverse=True)
  answer = str(int(''.join(numbers)))
  return answer

def comparator(a, b):
  n1 = int(a+b)
  n2 = int(b+a)
  return (n1 > n2) - (n1 < n2)
