# Section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# 파일 URL
img_url = "http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
html_url = "http://google.com"

# 다운받을 경로
save_path1 = "c:/test1.jpg" # png여도 된다.
save_path2 = "c:/index.html"
# 여기까지가 내가 가지고 올 이미지와 분석하고 싶은 홈페이지 url을 내 컴퓨터에 저장하는 것

# 예외 처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1) # 이미지 파일과 헤더값(이미 송,수신 정보)이 필요
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print("Download failed.") # 표시
    print(e) # 실질적으로 뭐가 에러가 났는 지 알려주는 것
else:
    # Header 정보 출력
    print(header1)
    print(header2) # attp?는 일회성 연결
    
    # 다운로드 파일 정보
    print("Filename1 {}".format(file1))
    print("Filename2 {}".format(file2))
    print()
    
    # # 성
    print("Download Succeed.") 