"""
Chapter 1
Python Advance(1) - Shallow Copy & Deep Copy
Keyword - shallow copy and deep copy

객체의 복사 종류 : Shallow Copy , Deep Copy
정확한 이해 후 사용 권장 -> 프로그래밍 개발 중요(문제 발생 요소)
가변 : list, set, dict
"""

# Ex1 Copy
# Call by value, Call by Refference, Call by Share


def disploy(title, firstValue, SecendValue):
    print(f"{title}", id(firstValue))
    print(f"{title}", id(SecendValue))

    print(f"{title}", firstValue)
    print(f"{title}", SecendValue)


a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list
disploy("Ex1 > ", a_list, b_list)

b_list[2] = 100
disploy("Ex1 > ", a_list, b_list)


b_list[3][2] = 1000
disploy("Ex1 > ", a_list, b_list)


# Ex2 - Shallow Copy
import copy

c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)
disploy("Ex2 > ", c_list, d_list)


d_list[2] = 100
disploy("Ex2 > ", c_list, d_list)

d_list[3][2] = 1000
disploy("Ex2 > ", c_list, d_list)

# Ex3 - Deep Copy

e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)
disploy("Ex3 > ", e_list, f_list)


f_list[2] = 100
disploy("Ex3 > ", e_list, f_list)

f_list[3][2] = 1000
disploy("Ex3 > ", e_list, f_list)
