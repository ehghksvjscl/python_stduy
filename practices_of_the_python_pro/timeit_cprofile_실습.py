"""
Cprofile(내장 패키지)
    python -m cProfile --sort cumtime timeit_cprofile_실습.py


"""

import random
from timeit import timeit

def sort_expensive():
    the_list = random.sample(range(1_000_000), 1_000)
    the_list.sort()


def sort_cheap():
    the_list = random.sample(range(1_000), 10)
    the_list.sort()


setup = 'from datetime import datetime'
statment = 'datetime.now()'
result = timeit(setup=setup, stmt=statment, number=1000)
sort_expensive()
for i in range(10):
    sort_cheap()

print(f"Took an average of {result / 1_000}s or {result}ms")
