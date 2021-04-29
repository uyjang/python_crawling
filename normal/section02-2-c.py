# Section02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ["c:/test1.jpg", "c:/index.html"]

# 다운로드 리소스 URL
target_url = ["http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg",
              "http://google.com"]

for i, url in enumerate(target_url): # enumerate를 쓰면 자동으로 내용 뿐만아니라 그 내용의 인덱스까지 보여줌
    # 예외 처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)  # open은 retrieve처럼 자료를 가져오지만 다운로드까지는 안해줌. 별도로 다운로드 코드를 작성해야하지만 다른 코드에서 사용할 수가 있음 / 리스폰스는 인스턴스 객체처럼 urlopen이 가지고 있는 기능도 다 쓸 수 있고 데이터도 가지고있음
        
        # 수신 내용
        contents = response.read()

        print('---------------------------------------------------')

        # 상태 정보 중간 출력
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print('---------------------------------------------------')

        # 파일 쓰기
        with open(path_list[i], 'wb') as c: # wb = write binary 의 약자 # 아까 다운로드가 안된다고 했으므로 여기서 별도로 다운로드가 되도록 하는 것임
            c.write(contents)

        # HTTP 에러 발생 시
    except HTTPError as e:
        print("Download failed.")
        print('HTTPError Code : ', e.code)

        # URL 에러 발생 시
    except URLError as e:
        print("Download failed.")
        print('URL Error Reason : ', e.reason)

        # 성공
    else:
        print()
        print("Download Succeed.")
