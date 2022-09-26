"""
객체 지향 프로그래밍 : 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
규모가 큰 프로젝트 : 함수로 프로그램 할 경우 -> 데이터 방대 -> 복잡 -> 유지보수 어려움
클래스 중심 : -> 데이터 중심 -> 객체로 관리
"""


class Car:
    """
    Car class
    Author : uno
    Date: 2022.09.27
    """

    def __init__(self, company: str, details: str) -> None:
        self._company = company
        self._details = details

    def __str__(self) -> str:
        return f"str : {self._company} - {self._details}"

    def __repr__(self) -> str:
        pass

    def detail_info(self):
        print(f"current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('가격')}")


car1 = Car("페라리", {"색": "흰", "파워": 400, "가격": 8000})
car2 = Car("bmw", {"색": "검", "파워": 270, "가격": 5000})
car3 = Car("아우디", {"색": "은", "파워": 300, "가격": 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dir__ 확인
print(dir(car1))
print(dir(car2))

print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(car1.__doc__)

# 실행
car1.detail_info()
car2.detail_info()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))
