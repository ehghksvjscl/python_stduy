"""
시퀀스형
컨테이너(Container : 서로 다른 자료형[List, tuple, collections.deque])
플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
가변(List, bytearray ,array.array, collections.deque, memoryview)
불변(tuple, str, bytes)
"""
# 해시 테이블(Hash Table)
# key에 Value를 저장하는 구조 (python 언어의 자체가 강력한 dict로 구성이 되어 있다.  ex __dict__)
# (엔진이 Hash로 되어 있다고 함)
# 파이썬 dict 해쉬 테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조!!*****
# key 값을 해싱 함수 -> 해쉬 주소 -> key에 대한 value 참조

# Dict 구조
print(__builtins__.keys())

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2)) # 가변형 이기에 hash값을 알 수 없다.

print()
print()

# Dict SetDefault 예제
source = (
    ("k1", "val"),
    ("k1", "va2"),
    ("k2", "va3"),
    ("k2", "va4"),
    ("k2", "va5"),
)

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의
new_dict3 = {k: v for k, v in source}
print(new_dict3)
