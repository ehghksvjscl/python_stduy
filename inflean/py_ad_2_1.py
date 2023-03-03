"""
Chapter 2
Python Advance(2) - Context Manager Annotation
Keyword - @contextlib.contextmanager

타이머 제작 예제(contextlib)
"""

# Ex1
# contextlib 사용

import contextlib


@contextlib.contextmanager
def write_file(fileName, method):
    f = open(fileName, method)
    yield f  # __enter__
    f.close()  # __exit__


with write_file("../data/test4.txt", "w") as f:
    f.write("Context Manager test4")

# Ex2
# contextlib 사용

import time


@contextlib.contextmanager
def excuteTimer(msg):
    startTime = time.monotonic()
    yield startTime
    endTime = time.monotonic()
    print(f"{msg} - {endTime - startTime}s")


with excuteTimer("시간 측정") as t:
    for i in range(100000000):
        pass
