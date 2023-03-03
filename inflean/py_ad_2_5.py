"""
챕터 2
 - Method Overloading
 - keyword - Overloading, oop, multiple dispatch

"""
"""
메소드 오버로딩 효과
1. 동일 메소드 재정의
2. 네이밍 기능 예측
3. 코드 절약, 가독성 향상
4. 메소드 파라미터 기반 호출 방식
"""

# Ex1
# 동일 이름 메소드 사용 예제
# 동적 타입 검사 -> 런타임에 실행(타입 에러가 실행시에 발견)


class SampleA:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

    # # 패킹으로 해결 가능 -> 마지막 add 함수가 실행됨
    # def add(self, *args):
    #     return sum(args)


# Ex2
# 타입 구분을 통한 add 함수 실행 class

sampleCode1 = SampleA()
print("Ex1 > ", sampleCode1.add(10, 20, 30))
# print("Ex1 > ", sampleCode1.add(10, 20))


class SampleB(object):
    def add(self, datatype, *args):
        if datatype == "int":
            return sum(args)

        elif datatype == "str":
            return " ".join(args)


sample2 = SampleB()
print("Ex2 > ", sample2.add("int", 10, 20, 30))
print("Ex2 > ", sample2.add("str", "hello", "world"))

# Ex3
# multipledispatch 패키지를 통한 메소드 오버로딩

from multipledispatch import dispatch


class Sample3(object):
    @dispatch(int, int)
    def mul(x, y):
        return x * y

    @dispatch(int, int, int)
    def mul(x, y, z):
        return x * y * z

    @dispatch(float, float, float)
    def mul(x, y, z):
        return x * y * z

    @dispatch(int, int)
    def add(x, y):
        return x + y

    @dispatch(str, str)
    def add(x, y):
        return " ".join([x, y])


sample3 = Sample3()
print(sample3.mul(10, 20))
print(sample3.mul(10, 20, 30))
print(sample3.mul(10.1, 20.2, 30.3))
print(sample3.add(10, 20))
print(sample3.add("hello", "world"))
