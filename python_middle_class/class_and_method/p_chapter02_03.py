"""
객체 지향 프로그래밍 : 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
규모가 큰 프로젝트 : 함수로 프로그램 할 경우 -> 데이터 방대 -> 복잡 -> 유지보수 어려움
클래스 중심 : -> 데이터 중심 -> 객체로 관리
"""


class Car:
    """
    Car class
    Author : uno
    Date: 2022.09.28
    Description : Class, Static, Instance Method
    """

    # 클레스 변수(모든 인스턴스가 공유)
    price_per_raise: float = 1.2

    def __init__(self, company: str, details: str) -> None:
        self._company = company
        self._details = details

    def __str__(self) -> str:
        return f"str : {self._company} - {self._details}"

    def __repr__(self) -> str:
        pass

    # Instance Method
    # self : 객체의 고유 속성 값을 사용
    def detail_info(self):
        print(f"current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('가격')}")

    # Instance Method
    def get_price(self):
        return "Before Car Price -> company : {}, price : {}".format(
            self._company, self._details.get("가격")
        )

    # Instance Method
    def get_price_culc(self):
        return "After Car Price -> company : {}, price : {}".format(
            self._company, self._details.get("가격") * Car.price_per_raise
        )

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Plezse Enter 1 Or More")
            return
        cls.price_per_raise = per
        print("success price update")

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == "bmw":
            return "Ok! This car is {}".format(inst._company)
        else:
            return "Sorry. This car is not bmw"


car1 = Car("페라리", {"색": "흰", "파워": 400, "가격": 8000})
car2 = Car("bmw", {"색": "검", "파워": 270, "가격": 5000})

car1.detail_info()
car2.detail_info()

# 가격 정보(직접 접근)
car1._details.get("price")
car2._details.get("price")

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 매소드 미사용)
Car.price_per_raise = 1.4

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상(클래스 매소드 사용)
Car.raise_price(1.6)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상(인스턴스 호출)
car1.raise_price(1.7)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 인스턴스 호출(스테이틱)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# 클래스 호출(스테이틱)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
