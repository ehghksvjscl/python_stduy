"""
챕터 4
 - 나만의 패키지 만들기(1)
키워드 - png(jpg) to gif, pill, image
"""

"""
패키지 작성
-> 정적이미지(JPG, PNG) -> GIF(애니메이션) 이미지 변환 패키지
"""

# glob -> 파일 리스트 가져오기[유사.os]
import glob

# pip install image 필요
from PIL import Image

# 이미지, 결과 생성 경로
path_in = "./project/images/*.png"
path_out = "./project/image_out/result.gif"

# 첫 번째 이미지 & 모든 이미지 리스트 패킹
# img, *images = [Image.open(f) for f in sorted(glob.glob(path_in))]
# 사이즈 조정
img, *images = [
    Image.open(f).resize((320, 240), Image.ANTIALIAS)
    for f in sorted(glob.glob(path_in))
]

# 이미지 저장
img.save(
    fp=path_out,
    format="GIF",
    append_images=images,
    save_all=True,
    duration=500,  # 변환 시간 (ms)
    loop=0,  # 반복 여부
)
