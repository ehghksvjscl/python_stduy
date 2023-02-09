"""
챕터 3
 - Meta Class Part2
키워드 - Type(name, base, dct), 다이나믹 메타클레스

"""

"""
메타클래스
1. 메타클래스 동적 생성 중요
2. 동적 생성한 메타클래스 -> 커스텀 메타클래스 생성
3. 의도하는 방향으로 직접 클래스 생성에 관여 할 수 있는 큰 장점
"""

# Ex1
# type 동적 클래스 생성 예제

# Name(이름), Bases(상송), Dct(속성, 메소드)
s1 = type("sample1", (), {})

print("Ex1 > ", s1)
print("Ex1 > ", type(s1))
print("Ex1 > ", s1.__base__)
print("Ex1 > ", s1.__dict__)

# 동적 생성 + 상속
class Parent1:
    pass


s2 = type(
    "sample2",
    (Parent1,),
    dict(
        attr1=100,
        attr2="hello",
    ),
)

print("Ex2 > ", s2)
print("Ex2 > ", type(s2))
print("Ex2 > ", s2.__base__)
print("Ex2 > ", s2.__dict__)
print("Ex2 > ", s2.attr1, s2.attr2)

# Ex2
# type 동적 클래스 생성 + 메소드 추가


class SampleEx:
    attr1 = 30
    attr2 = 100

    def add(self, n, m):
        return n + m

    def mul(self, n, m):
        return n * m


ex = SampleEx()
print("Ex2 > ", ex.attr1)
print("Ex2 > ", ex.attr2)
print("Ex2 > ", ex.add(10, 20))
print("Ex2 > ", ex.mul(10, 20))

print()

s3 = type(
    "Sample3",
    (),
    dict(
        attr1=100,
        attr2=200,
        add=lambda x, y: x + y,
        mul=lambda x, y: x * y,
    ),
)

print("Ex2 > ", s3.attr1)
print("Ex2 > ", s3.attr2)
print("Ex2 > ", s3.add(10, 20))
print("Ex2 > ", s3.mul(100, 20))
