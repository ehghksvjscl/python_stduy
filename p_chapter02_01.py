"""
객체 지향 프로그래밍 : 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
규모가 큰 프로젝트 : 함수로 프로그램 할 경우 -> 데이터 방대 -> 복잡 -> 유지보수 어려움
클래스 중심 : -> 데이터 중심 -> 객체로 관리
"""

# 일반적인 코딩 (안좋음. 데이터 많아 지면 관리 힘듬)
# 차량 1
car_company_1 = "페라리"
car_detail_1 = [{"색갈": "흰색"}, {"마력": 400}, {"가격": 8000}]

# 차량 2
car_company_2 = "BMW"
car_detail_2 = [{"색갈": "검정"}, {"마력": 270}, {"가격": 8000}]

# 차량 3
car_company_3 = "아우디"
car_detail_3 = [{"색갈": "은색"}, {"마력": 300}, {"가격": 6000}]


# 리스트 구조
# 관리 하기 불편
# 인덱스로 접근 해야 해서 사용이 불편~~
car_company_list = ["페라리", "BMW", "아우디"]
car_company_detail_list = [
    {
        "색갈": "흰색",
        "마력": 400,
        "가격": 8000,
    },
    {
        "색갈": "검정",
        "마력": 270,
        "가격": 8000,
    },
    {
        "색갈": "은색",
        "마력": 300,
        "가격": 6000,
    },
]

del car_company_list[1]
del car_company_detail_list[1]

print(car_company_list)
print(car_company_detail_list)

print()
print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(key)
car_dicts = [
    {
        "car_company": "페라리",
        "company_detail": {
            "색갈": "흰색",
            "마력": 400,
            "가격": 8000,
        },
    },
    {
        "car_company": "BMW",
        "company_detail": {
            "색갈": "검정",
            "마력": 270,
            "가격": 8000,
        },
    },
    {
        "car_company": "아우디",
        "company_detail": {
            "색갈": "은색",
            "마력": 300,
            "가격": 6000,
        },
    },
]

del car_dicts[1]
print(car_dicts)


class Car:
    def __init__(self, company: str, details: str) -> None:
        self._company = company
        self._details = details

    def __str__(self) -> str:
        return f"str : {self._company} - {self._details}"

    def __repr__(self) -> str:
        pass


car1 = Car("페라리", {"색": "흰", "파워": 400, "가격": 8000})
car2 = Car("bmw", {"색": "검", "파워": 270, "가격": 5000})
car3 = Car("아우디", {"색": "은", "파워": 300, "가격": 6000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)


car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

# 반목문(__str__)
for x in car_list:
    print(repr(x))
    print(x)
