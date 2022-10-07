"""
병행성(Concurrency)
이터레이터, 제네레이터
Iterator, Generator
"""

# 파이썬 반복 가능한 타입
# collections, text file, List, Dict, Set, Tuple, unpacking, *args... : iterable)

# 반복 가능한 이유? -> iter(x) 함수 호출 가능
from typing import Iterable


t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(dir(t))

for c in t:
    print(c, end="")


print("")

# while
w = iter(t)

while True:
    try:
        print(next(w), end="")
    except StopIteration:
        break

print()
print(hasattr(t, "__iter__"))
print(isinstance(t, Iterable))  # t가 Iterable을 상속을 받았는지?

print()
print()

# next 페턴
class WordSplitter:
    def __init__(self, text: str) -> None:
        self._idx = 0
        self._text = text.split(" ")

    def __next__(self):
        print("Called __next__")
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration("Stopped Iteration")

        self._idx += 1
        return word

    def __repr__(self) -> str:
        return "WordSplit(%s)" % (self._text)


w1 = WordSplitter("Do today what you could do tommorrow")
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용양 증가
#    그래서 제너레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Corotine) 구현과 연동
# 3. 작은 메모리 조각 사용


class WordSplitGenator:
    def __init__(self, text: str) -> None:
        self._text = text.split(" ")

    def __iter__(self):
        for word in self._text:
            yield word  # 제너리이터
        return

    def __repr__(self) -> str:
        return "WordSplitGenerator(%s)" % (self._text)


wg = WordSplitGenator("Do today what you could do tommorrow")
wt = iter(wg)

print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
