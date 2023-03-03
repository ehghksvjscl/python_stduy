"""
Chapter 1
Python Advance(1) - Context Manager(1)
Keyword - Contextlib __enter__, __exit__

타이머 제작 예제
"""

# Ex1
# Use Class

import time


class ExcuteTimer(object):
    def __init__(self, msg) -> None:
        self.msg = msg

    def __enter__(self):
        self.startTime = time.monotonic()
        return self.startTime

    def __exit__(self, exc_type: bool, value, tace_back):
        endTime = time.monotonic()
        if exc_type:
            print(f"Logging exception {exc_type} - {value} - {tace_back}")
        else:
            print(f"{self.msg} - {endTime - self.startTime}s")

        return True


with ExcuteTimer("test1") as a:
    print("test1")
    raise Exception("test1 error")
