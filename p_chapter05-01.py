"""
일급 함수
파이썬 함수 특징
    1. 런터임 초기화
    2. 변수 할당 가능
    3. 함수 인수 전달 가능
    4. 함수 결과 반화 가능(return)
"""

# 함수 객체(펙토리얼)
def factorial(n: int):
    """Factorial Funtion"""

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

print()
print()

var_func = factorial

print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 11))))

# reduce
from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))

# 익명함수(Lambda)
# 가급적 주석 작성
# 가급적 함수 작성
# 일반 함수 형태로 리펙토링 권장

print(reduce(lambda x, y: x + y, range(1, 11)))

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(
    callable(str),
    callable(list),
    callable(var_func),
    callable(factorial),
    callable(3.14),
)

# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from functools import partial
from operator import mul

print(mul(10, 10))
five = partial(mul, 5)

six = partial(five, 6)

print(five(10))
print(six())
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))
