"""
Special Method(Magic Method)
파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
클래스안에 정의할 수 있는 특별한(Built-in) Method
"""

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(n + 100, n.__add__(100))
# print(n.__doc__)
print(bool(n), n.__bool__())
print(n * 100, n.__mul__(100))

print()
print()

# 클래스 예제1
class Fruit:
    def __init__(self, name: str, price: int) -> None:
        self._name = name
        self._price = price

    def __str__(self) -> str:
        return "Fruit Class Info : {} {}".format(self._name, self._price)

    def __add__(self, instance: object) -> int:
        return self._price + instance._price

    def __sub__(self, instance: object) -> int:
        return self._price - instance._price

    def __le__(self, instance: object) -> bool:
        if self._price <= instance._price:
            return True
        else:
            return False

    def __ge__(self, instance: object) -> bool:
        if self._price >= instance._price:
            return True
        else:
            return False


# 인스턴스 생성
s1 = Fruit("오렌지", 7500)
s2 = Fruit("바나나", 3000)

# 일반적인 계산
print(s1._price + s2._price)

# __add__ Method 계산
print(s1 + s2)

# __sub__ Method 계산
print(s1 - s2)
print(s2 - s1)

# __le__ Method 계산
print(s1 >= s2)

# __ge__ Method 계산
print(s1 <= s2)
