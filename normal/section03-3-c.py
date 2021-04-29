# Section03-3
# 기본 스크랩핑 실습
# 다음 주식 정보 가져오기

import json # 스크랩핑할 데이터 형식이 제이손 형식
import urllib.request as req
from fake_useragent import UserAgent


# Fake Header 정보(가상으로 User-Agent 생성)
ua = UserAgent()
# print(ua.ie)
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)
# print(ua.random)


# 헤더 선언
headers = {
    'User-Agent': ua.ie,
    'referer': 'https://finance.daum.net/' # 가장 처음에 들어왔던 사이트 / 나는 여기를 통해 들어왔어요~ 라는 의미
}

# 다음 주식 요청 URL
url = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8') # req모듈안의 Request클래스를 불러와서 인자를 넣음.

# 응답 데이터 확인(Json Data)
# print('res', res)

# 응답 데이터 str -> json 변환 및 data 값 저장
rank_json = json.loads(res)['data']

# 중간 확인
print('중간 확인 : ', rank_json, '\n')

for elm in rank_json:
    # print(type(elm)) #Type 확인
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm['tradePrice'], elm['name']), )

# 파일 저장 해보기
