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
