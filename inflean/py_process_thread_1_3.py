"""
    챕터 1
    Multithreading - Thread(1) Basic
    키워드 : Threading basic

"""

import logging
import threading
import time

# 쓰레드 실행 함수
def thread_func(name):
    logging.info("Sub-Thread %s: starting", name)
    time.sleep(3)
    logging.info("Sub-Thread %s: finishing", name)


# 메인 영역
if __name__ == "__main__":
    # Logging Format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=format,
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.info("Main-Thread: before creating thread")

    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=("first",))
    logging.info("Main-Thread: before runing thread")

    # 서브 스레드 실행
    x.start()

    # 주석 전후 결과 확인
    x.join()

    logging.info("Main-Thread: wait for the thread to finish")
    logging.info("Main-Thread: all done")
