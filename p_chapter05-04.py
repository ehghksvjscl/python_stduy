"""
일급 함수
클로저 심화
왜부에서 호출된 함수의 변수값, 상태(레퍼러스) 복사 후 저장 -> 후에 접근(엑세스) 가능
"""

# Closure
def closure_ex1():
    # Free variable
    # 클로저 영역
    series = []

    def averager(v):
        series.append(v)
        print("inner >>> {} / {}".format(series, len(series)))

        return sum(series) / len(series)

    return averager


avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(20))
print(avg_closure1(30))

print()
print()

# function inspection
print(dir(avg_closure1))
print(avg_closure1.__code__.co_freevars)
print(avg_closure1.__closure__[0].cell_contents)

print()
print()

# 잘못된 클로저 사용의 예
def closure_ex2():
    # 자유 변수
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure2 = closure_ex2()

# print(avg_closure2(10))


def closure_ex3():
    # 자유 변수
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure3 = closure_ex3()
print(avg_closure3(10))
