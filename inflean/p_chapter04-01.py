"""
시퀀스형
컨테이너(Container : 서로 다른 자료형[List, tuple, collections.deque])
플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
가변(List, bytearray ,array.array, collections.deque, memoryview)
불변(tuple, str, bytes)
"""

# 지능형 리스트(Comprehending Lists)
chars = "+_)(*&^%$#@!"
code_list1 = [ord(s) for s in chars]

print(code_list1)

# Comprehending Lists + Map, Filter
code_list2 = [ord(s) for s in chars if ord(s) > 40]
print(code_list2)

code_list3 = list(filter(lambda x: x > 40, map(ord, chars)))
print(code_list3)

# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])

# Generator 생성
import array

# Generator : 한 번에 한개의 항목을 생성(메모리 유지 X)
tuple_g = (ord(s) for s in chars)
array_g = array.array("I", (ord(s) for s in chars))

print(tuple_g.__next__())
print(tuple_g.__next__())
print(array_g)
print(type(array_g))
print(array_g.tolist())

# 제너레이터 예제
students = (c + str(n) for c in "A B C D".split() for n in range(1, 21))
for s in students:
    print(s)

# 리스트 주의 (얕은 복사, 깊은 복사)
marks1 = [["~"] * 3 for _ in range(4)]
marks2 = [["!"] * 3] * 4

print(marks1)
print(marks2)

# 수정 (수정된 값이 다르다.)
marks1[0][1] = "X"
marks2[0][1] = "X"

print(marks1)
print(marks2)

# 증명 id 값이 다르다..
print([id(i) for i in marks1])
print([id(1) for i in marks2])
