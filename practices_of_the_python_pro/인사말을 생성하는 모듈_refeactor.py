from datetime import datetime


def day():
    today_weekday = datetime.today().strftime("%A")
    print(today_weekday)


def part_of_day():
    current_hour = datetime.today().hour
    if current_hour < 12:
        print("아침")
    elif current_hour > 12 and current_hour < 17:
        print("오후")
    else:
        print("저녁")


class Greeter:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self, store):
        print(f"Hi my name is {self.name}, and welcome to {store}")
        print(f"How\'s your {day()} {part_of_day()} going?")
        print(f"Here\'s a coupon for 20% off!")


greeter = Greeter("uno")
greeter.greet("kidsnote")
