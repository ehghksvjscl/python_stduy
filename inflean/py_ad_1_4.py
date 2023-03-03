"""
Chapter 1
Python Advance(1) - Context Manager(1)
Keyword - Contextlib __enter__, __exit__ exception

컨택스트 매니저 : 원하는 타이밍 정확하게 리소스를 할당 및 제공, 변환하는 역활
가장 대표적인 with 구문 이해
"""

# Ex1(with이 나오기 이전)
file = open("../data/test1.txt", "w")
try:
    file.write("Context Manager test1")
finally:
    file.close()

# Ex2(with이 나온 후)
with open("../data/test2.txt", "w") as f:
    f.write("Context Manager test2")

# Ex3
# Use Class -> Context Manager with exception handling


class MyFileWriter:
    def __init__(self, fileName, method) -> None:
        print("MyFileWriter started : __init__")
        self.fileObj = open(fileName, method)

    def __enter__(self):
        print("MyFileWriter started : ____enter____")
        return self.fileObj

    def __exit__(self, exc_type: bool, value, tace_back):
        print("MyFileWriter ended : ____exit____")
        if exc_type:
            print(f"Logging exception {(exc_type, value, tace_back)}")
        self.fileObj.close()


with MyFileWriter("../data/test3.txt", "w") as f:
    f.write("Context Manager test3")
