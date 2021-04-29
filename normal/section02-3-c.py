# Section02-3
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(1)

import requests
import lxml.html


def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인 함수
    """
    # 세션 사용 권장
    # session = requests.Session()
    # session.get('https://www.naver.com/')

    # 스크랩핑 대상 URL
    response = requests.get('https://www.naver.com/') # get,post 방식이 있음 / request.get은 response = request.urlopen()한 다음 contents = response.read()와 기능이 비슷함.
    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)
    # 결과 출력
    for url in urls:
        print(url)


def scrape_news_list_page(response):
    # URL 리스트 선언
    urls = [] # 여기에 url정보들을 담는다.
    # 태그 정보 문자열 저장
    root = lxml.html.fromstring(response.content) # lxml안에 html을 처리하고 프롬스트링이라고 하는(문자열로부터 입력을 받고 ) 거 안에 리스폰스.컨텐트를 넣음

    # 문서내 경로 절대 경로 변환
    # root.make_links_absolute(response.url)

    for a in root.cssselect('.api_list .api_item a.api_link'): # 루트라는 변수안에 있는 css만 선택해주는 cssselect라는 함수?를 실행하는 것 
        # 링크 
        url = a.get('href')
        # 리스트 삽입
        urls.append(url)
    return urls


# 스크랩핑 시작
if __name__ == '__main__': # 이거 없이는 아무것도 실행이 되지 않음
    main()
