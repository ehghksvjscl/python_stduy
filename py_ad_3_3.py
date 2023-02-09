"""
챕터 3
 - Meta Class Part 3
키워드 - type inheritance, Custom metaclass

"""

"""
메타클래스 상속
1. type class 상속
2. metaclass 상속 사용
3. Custom metaclass 생성
"""

# Ex1
# Custom MetaClass 생성(type 상속 X)


def cus_mul(self, d):
    for i in range(len(self)):
        self[i] *= d


def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


CustomList = type(
    "CustomList",
    (list,),
    dict(
        desc="커스텀 리스트1",
        cus_mul=cus_mul,
        cus_replace=cus_replace,
    ),
)

c1 = CustomList([1, 2, 3, 4, 5])
c1.cus_mul(10)
c1.cus_replace(10, 777)

print("Ex1 > ", c1)
print("Ex1 > ", c1.desc)
print("Ex1 > ", dir(c1))

# Ex2
# 메타클레스는 99%의 사용자는 전혀고려할 필요가 없는 흑마법입니다.
# 만약 당신이 이게 정말로 필요할지에 대해 의문을 같는다면, 필요하지 않습니다.
# (이게 필요한지 아는 사람은 이미 모든 내용을 알고 있을것입니다.)

# Custom MetaClass 생성(type 상속 O)
# 실행 순서 new -> init -> call
class CustomListMeta(type):
    # 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, namespace):
        print("__init__", self, object_or_name, bases, namespace)
        super().__init__(object_or_name, bases, namespace)

    # 인스턴스 실행
    def __call__(self, *args, **kwds):
        print("__call__", self, args, kwds)
        return super().__call__(*args, **kwds)

    # 클래스 인스턴스 생성(메모리 할당)
    def __new__(mcs, name, bases, namespace, **kwds):
        print("__new__", mcs, name, bases, namespace, kwds)
        return super().__new__(mcs, name, bases, namespace)


CustomList2 = CustomListMeta(
    "CustomList2",
    (list,),
    dict(
        desc="커스텀 리스트1",
        cus_mul=cus_mul,
        cus_replace=cus_replace,
    ),
)

c2 = CustomList([1, 2, 3, 4, 5])
c2.cus_mul(10)
c2.cus_replace(10, 777)

print("Ex2 > ", c2)
print("Ex2 > ", c2.desc)
print("Ex2 > ", dir(c2))
