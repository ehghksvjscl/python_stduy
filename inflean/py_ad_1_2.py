"""
Chapter 1
Python Advance(1) - Lambda, Reduce, Map, Filter Functions
Keyword - lambda, map, filter, reduce
"""

# Lambda 장점 ㅣ 익명, 힙 영역 사용 즉시 소멸(메모리 절약), pythonic?, 파이썬 가비지 컬렉션(Count=0)
# 일반 함수 : 재사용성 위해 메모리 저장
# 시퀀스형 전처리에 Reduce, Map, Filter 주로 사용

# Ex1
cul = lambda a, b, c: a * b + c
print("Ex1 > ", cul(10, 15, 20))

# Ex2
digits1 = [x * 10 for x in range(1, 11)]
print("Ex2 > ", digits1)

result = map(lambda i: i**2, digits1)
print("Ex2 > ", list(result))


def also_square(nums):
    def double(x):
        return x**2

    return list(map(double, nums))


print("Ex2 > ", also_square(digits1))

# Ex3
digits2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, digits2))
print("Ex3 > ", result)


def also_evens(nums):
    def even(num):
        if num % 2 == 0:
            return num

    return list(filter(even, nums))


print("Ex3 > ", also_evens(digits2))

# Ex4
from functools import reduce

digits3 = [x for x in range(1, 101)]
result = reduce(lambda total, x: total + x, digits3)

print("Ex4 > ", result)


def also_add(nums):
    def total(x, y):
        return x + y

    return reduce(total, nums)


print("Ex4 > ", also_add(digits3))
