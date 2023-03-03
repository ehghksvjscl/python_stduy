"""
    챕터 1
    Multithreading - Python GIL(Global Interpreter Lock)
    키워드 : Cpython, 메모리관리, GIL 사용 이유

"""
"""
GIL(Global Interpreter Lock)
    (1). Cpython -> Python(bytecode) 실행 시 여러 thread 사용할 경우
        - 단일 스레드만이 python object에 접근하게 제한하는 mutex
    (2). Cpython 메모리 관가 취약 하기 때문(즉, thread-safe)
    (3). 단일 스레드로 충분히 빠르다.
    (4). 프로세스 사용 가능(Numpy, Scipy) 등 Gil 외부 영역에서 효율적인 코딩
    (5). 병렬 처리는 Multiprocessing, asyncio 선택지 다양함.
    (6). thread 동시성 완벽 처리를 위해 -> Jython, IronPython 등이 존재
    
"""
