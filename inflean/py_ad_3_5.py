"""
챕터 3
 - Descriptor(1)
키워드 - descriptor vs property, low level(discriptor), high level(property)

"""

"""
Descriptor

1. 상황에 맞는 메소드 구현을 통한 객체지향 프로그래밍 구현
2. property와 달리 재사용 가능
3. ORM freamwork에서 사용
"""

# Ex1
# Descriptor 예제

import os


class DirectoryFileCount:
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))


class DirectoryPath:
    """Descriptor Instance"""

    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname


s = DirectoryPath("./")
g = DirectoryPath("../")

print(s.size)
print(g.size)

# Ex2
# Descriptor 예제2

import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)


class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value

    def __get__(self, obj, objtype=None):
        logging.info("Accessing %r giving %r", "score", self.value)
        return self.value

    def __set__(self, obj, value):
        logging.info("Updating %r giving %r", "score", self.value)
        self.value = value


class Student:
    score = LoggedScoreAccess()

    def __init__(self, name):
        self.name = name


s1 = Student("Kim")
s2 = Student("Park")

# 학생1 확인
print("Ex2 >", s1.score)
s1.score += 20
print("Ex2 >", s1.score)

# 학생2 확인
print("Ex2 >", s2.score)
s2.score += 30
print("Ex2 >", s2.score)

# __dict__ 확인
print("Ex2 >", vars(s1))
print("Ex2 >", vars(s2))
print("Ex2 >", s1.__dict__)
print("Ex2 >", s2.__dict__)
