"""
Chapter 1
Python Advance(1) - Python Variable Scope
Keyword - scope, global, nonlocal, locals, globals
"""

"""
전역변수는 주로 변하지 않는 고정 값에 사용
지역변수 사용 이유 : 지역변수는 함수 내에 로직 해결에 국한, 소멸주기 : 함수 실행 해제 시
전역변수를 지역내에서 수정되는 것을 권장 하지 않는다.
"""

# Ex1
a = 10  # Global variable


def foo():
    # Read global variable
    print("Ex1 > ", a)


foo()
print("Ex1 > ", a)

# Ex2
b = 20


def bar():
    b = 30  # Local variable
    print("Ex2 > ", b)  # Read local variable


bar()
print("Ex2 > ", b)

# Ex3
c = 40


def foobar():
    # c = c + 10 # UnboundLocalError
    print("Ex3 > ", c)


foobar()

# Ex4
d = 50


def barfoo():
    global d
    d += 100
    print("Ex4 >", d)


barfoo()
print("Ex4 >", d)

# Ex5(중요)
def outer():
    e = 70

    def inner():
        nonlocal e
        e += 10
        print("Ex5 > ", e)

    return inner


in_test = outer()  # Closure
in_test()
in_test()
in_test()

# Ex6
def func(var):
    x = 10

    def printer():
        print("Ex6 >", "Printer Func Inner")

    print("Func Inner", locals())


func("Hi")

# Ex7
print("Ex7 >", globals())
globals()["test_variable"] = 10
print(test_variable)

# Ex8(지역 -> 전역 변수 생성)
for i in range(1, 11):
    for k in range(1, 11):
        globals()["plus_{}_{}".format(i, k)] = i * k

print(globals())
print(plus_3_3)
