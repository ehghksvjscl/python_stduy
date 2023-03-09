# 단락을 문장과, 토크으로 분해
import re

product_review = '''This is a fine milk, but the product
line appears to be limited in available colors. I
could only find white.'''

# compile: 정규식을 등록 한다.
# findall : 등록한 정규식을 적용하여 find한다.
# match : 문자열의 처음부터 정규식과 매치되는지 조사한다.
# re.DOTALL 옵션은 여러 줄로 이루어진 문자열에서 줄바꿈 문자에 상관없이 검색할 때 많이 사용한다.
sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)
matches = sentence_pattern.findall(product_review)
sentences = [match[0] for match in matches]

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    matches = word_pattern.findall(sentence)
    words = [match[0] for match in matches]
    print(words)