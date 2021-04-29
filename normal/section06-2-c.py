# Section06-2
# Selenium
# Selenium 사용 실습(2) - 실습 프로젝트(1)

# selenium 임포트
import time
from selenium import webdriver
from selenium.webdriver.common.by import By # 언제언제까지라는 뜻으로 wait기능을 쓸 때 BY가 사용됨 
from selenium.webdriver.support.ui import WebDriverWait # 브라우저가 검색을 시작하고 전부 로딩할 때까지 기다려주는 기능
from selenium.webdriver.support import expected_conditions as EC # 어떤 상태가 될때까지 예상하는 기능으로 위의 by랑 wait랑 함께 사용된다.
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless") # 브라우저가 뜨면서 실행되는 모습을 안보여주고 데이터를 콘솔창에 보여주는 기능

# webdriver 설정(Chrome, Firefox 등) - Headless 모드
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe', options=chrome_options)

# webdriver 설정(Chrome, Firefox 등) - 일반 모드
# browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)  # maximize_window(), minimize_window()

# 페이지 이동
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용
# print('Before Page Contents : {}'.format(browser.page_source))

# # 제조사별 더 보기 클릭1
# # Explicitly wait
WebDriverWait(browser, 10) \
    .until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()
    # 웹드라이버를 3초동안 기다리지만 3초 안에 기대상황(EC, 여기에서는 모든 구성요소들이 자기 자리를 찾고 화면에 뜨는 상황)이 발생하면 xpath에 지정한 요소를 클릭하겠다 라는 뜻.
    # 3초가 넘어가도 안뜨면 에러가 뜨면서 프로그램이 종료됨.

# # 제조사별 더 보기 클릭2
# # Implicitly wait
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# # 원하는 모델 카테고리 클릭
WebDriverWait(browser, 10) \
    .until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[15]/label'))).click()

# # 2차 페이지 내용
# print('After Page Contents : {}'.format(browser.page_source))

time.sleep(3)

# # bs4 초기화
soup = BeautifulSoup(browser.page_source, "html.parser")

# # 소스코드 정리
# print(soup.prettify())

# # 메인 상품 리스트 선택
pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

# # 상품 리스트 확인
# print(pro_list)

# # 필요 정보 추출
for v in pro_list:
#     # 임시 출력
    print(v)

# #     # 불필요한 영역 패스
    if not v.find('div', class_='ad_header'):
# #         # 태그 정보 출력
#         # print('Name : {}, Img : {}, Price : {}'.format(v.select('p.prod_name > a'), v.select('a.thumb_link > img'), v.select('p.price_sect > a')))

# #         # 상품명, 이미지, 가격
        print(v.select('p.prod_name > a')[0].text.strip())
        print(v.select('a.thumb_link > img')[0]['src'])
        print(v.select('p.price_sect > a')[0].text.strip())

#     print()

# # 브라우저 종료
browser.quit()
