"""
네임드 튜플!!
"""

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)


# 두점 사이의 거리 구하기
from math import sqrt
from msilib.schema import Class

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# 네임드 튜플 사용
from collections import namedtuple

Point = namedtuple("Point", "x y")
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_leng2)

# 네임드 튜플 사용 방법
Point1 = namedtuple("Point", ["x", "y"])
Point2 = namedtuple("Point", "x,y")
Point3 = namedtuple("Point", "x y")
# class는 약속된 이름이기에 rename을 붙여야 한다.
Point4 = namedtuple("Point", "x y z class", rename=True)

# 출력
print(Point1, Point2, Point3, Point4)

# dict to unpacking
temp_dict = {"x": 75, "y": 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)
print()

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

# 사용
print(p1[0], p2[1])
print(p1.x, p2.y)

# Unpacking
x, y = p2

print(x, y)

# 네임드 튜플 메소드
temp_list = [52, 38]

p6 = Point2._make(temp_list)
print(p6)

# _fields: 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)

# _acdict() : dict 반환 python 3.8이상은 dict 반환
# python vsersion 3.8 미만일 경우 Orderdict 반환
print(p1._asdict())
print(p4._asdict())

# 실사용 실습
# 반20명, 4개의 반(A,B,C,D)

Classes = namedtuple("Classes", "rank number")

ranks = "A B C D".split()
numbers = [n for n in range(1, 21)]

# 리스트 컨플레인션
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))

# 추천
students2 = [
    Classes(rank, number)
    for rank in "A B C D".split()
    for number in [n for n in range(1, 21)]
]

print(len(students2))

for s in students2:
    print(s)
