"""
시퀀스형
컨테이너(Container : 서로 다른 자료형[List, tuple, collections.deque])
플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
가변(List, bytearray ,array.array, collections.deque, memoryview)
불변(tuple, str, bytes)
"""
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*divmod(100, 9))

print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

print(l, id(l))
print(m, id(m))

# sort vs sorted
# reverse, key=len, key=str.Lower, key=func...

# sorted : 정렬 후 새로운 객체 반환(원본 불면경)
f_list = ["orange", "apple", "mango", "papaya", "lemon", "strawberry", "coconut"]

print("sorted - ", sorted(f_list))
print("sorted - ", sorted(f_list, reverse=True))
print("sorted - ", sorted(f_list, key=len))
print("sorted - ", sorted(f_list, key=lambda x: x[-1]))  # 끝글자
print("sorted - ", sorted(f_list, key=lambda x: x[-1], reverse=True))
print("sorted - ", f_list)

# sort : 정렬 후 객체 직업 변경(원본 변경)
print("sort - ", f_list.sort(), f_list)
print("sort - ", f_list.sort(reverse=True), f_list)
print("sort - ", f_list.sort(key=len), f_list)
print("sort - ", f_list.sort(key=lambda x: x[-1]), f_list)
print("sort - ", f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

# List vs Array 적합 한 사용 방법
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# array 기반 : 숫자 자료형일때 ... web에서는 잘안쓸듯
