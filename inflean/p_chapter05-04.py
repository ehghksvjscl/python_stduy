"""
일급 함수
데코레이터(Decorator)

장점 : 중복제거, 코드 간결, 
       공통 함수 작성
       로깅, 프레임워크, 유효성 체크 -> 공통 함수

단점 : 가독성 감소?, 
       특정 기능에 한정 된 함수는 -> 단일 함수가 유리
       디버깅 불편
"""

# 데코레이터 실습
import time


def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()

        # 함수 실행
        result = func(*args)

        et = time.perf_counter() - st

        # 실행 함수명
        name = func.__name__

        # 함수 메게 변수
        arg_str = ", ".join(repr(arg) for arg in args)

        # 결과 출력
        print("[%0.5fs] %s(%s) -> %r" % (et, name, arg_str, result))

        return result

    return perf_clocked


@perf_clock
def time_func(seconds):
    time.sleep(seconds)


@perf_clock
def sum_func(*numbers):
    return sum(numbers)


# 데코레이터 미사용
non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)

print(non_deco1, non_deco1.__code__.co_freevars)
print(non_deco2, non_deco2.__code__.co_freevars)

print("-" * 40, "Called None Decorator -> time_func")
print()
non_deco1(0.5)

print("-" * 40, "Called None Decorator -> sum_func")
print()
non_deco2(100, 200, 300, 400, 500)

print()
print()

# 데코레이터 사용
print("-" * 40, "Called Decorator -> time_func")
time_func(0.5)

print("-" * 40, "Called None Decorator -> sum_func")
sum_func(100, 200, 300, 400, 500)
