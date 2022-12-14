"""
Special Method(Magic Method)
파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
클래스안에 정의할 수 있는 특별한(Built-in) Method
"""

from __future__ import annotations

# 클래스 예제2
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 = (50 , 15)
# Max((5, 10)) = 10


class Vector(object):
    def __init__(self, *args: tuple):
        """
        Create a vector
        example : v = Vactor(5, 10)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self: Vector) -> str:
        """Return the vector Informations"""
        return f"Vector({self._x}. {self._y})"

    def __add__(self, other: Vector) -> Vector:
        """Return added the vector"""
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, n: int) -> Vector:
        return Vector(self._x * n, self._y * n)

    def __bool__(self) -> bool:
        return bool(max(self._x, self._y))


# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# 메직메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2), bool(v3))
