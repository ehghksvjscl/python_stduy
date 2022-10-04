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
