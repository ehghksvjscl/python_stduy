"""
챕터 3
 - Descriptor(1)
키워드 - descriptor, get, set, property

"""

"""
Descriptor

1. 객체에서 서로다른 객체를 속성값으로 가지는 것
2. Read, Write, Delete 등을 미리 정의
3. data descriptor(set, del), non-data descriptor(get)
4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 설계 가능
"""


def display(cls):
    # 선언
    result = cls()

    # GET 호출
    print(result.name)

    # SET 호출
    result.name = "test"
    print(result.name)
    # result.name = 10 -> TypeError

    # DELETE 호출
    del result.name
    print(result.name)


class DiscriptorEx1(object):
    def __init__(self, value="default"):
        self.value = value

    def __get__(self, obj, objtype):
        return f"Get method called -> {obj}, {objtype}, {self.value}"

    def __set__(self, obj, value):
        print("Set method called")
        if isinstance(value, str):
            self.value = value
        else:
            raise TypeError("Must be a string")

    def __delete__(self, obj):
        print("Delete method Called")
        self.value = None


class Sample1(object):
    name = DiscriptorEx1()


display(Sample1)

# Ex2
# Property 클래스 사용 Descriptor 직접 구현
# class property(fget=None, fset=None, fdel=None, doc=None):


class DiscriptorEx2(object):
    def __init__(self, value="default"):
        self.value = value

    def getValue(self):
        return f"Get method called -> {self}, {self.value}"

    def setValue(self, value):
        print("Set method called")
        if isinstance(value, str):
            self.value = value
        else:
            raise TypeError("Must be a string")

    def DeleteValue(self):
        print("Delete method Called")
        self.value = None

    name = property(getValue, setValue, DeleteValue, "Property Example")


display(DiscriptorEx2)
