import scrapy
import logging # 파이썬에서 사용하는 패키지형태로 사용하기 위해서 임포트한 것

# 커맨시 실행시 --logfile 파일명, --nolog
logger = logging.getLogger('mylogger1')


# 스파이더 종류 : CrawlSpider, XMLFeedSpider, CSVFeedSpider, SitemapSpider
class TestSpider(scrapy.Spider):
    # 스파이더 네임 (중복 허용X, 스파이더 실행 시 사용)
    name = 'test4'
    # 크롤링 허용 도메인(리스트 가능)
    allowed_domains = ['blog.scrapinghub.com', 'daum.net', 'naver.com']
    # 크롤링 대상 URLS(멀티 사용 가능)
    # 싱글 도메인
    # start_urls = ['http://blog.scrapinghub.com/']

    # 실행 방법1
    # 멀티 도메인
    start_urls = ['https://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']

    # 사용자 시스템 설정(settings.py)
    custom_settings = {
        'DOWNLOAD_DELAY': 2
    }

    # 실행 방법2
    # Request 각각 지정
    # def start_requests(self):
    #     yield scrapy.Request('http://blog.scrapinghub.com/', self.parse)
    #     yield scrapy.Request('https://naver.com', self.parse)
    #     yield scrapy.Request('https://daum.net', self.parse)

    def parse(self, response):
        # print(response)
        # # 방법1(파이썬 패키지)
        # logger.info('Response URL1 : %s' % response.url)
        # logger.info('Response Status Code1 : %s' % response.status)

        # # 방법2(Spider logger 사용) # print보다 보기 좋게 출력됨
        # self.logger.info('Response URL2 : %s' % response.url)
        # self.logger.info('Response Status Code2 : %s' % response.status)

        if response.url.find('scrapinghub'):
            yield {
                'sitename': response.url,
                'contents': response.text[:100]
                # 'test': response.css('').get() # 여러 사이트에서 크롤링을 동시헤 하고 싶을 때 리스폰스 분기를 이용 하는데 이때 이 코드에 내가 가져올 css가 뭔 지 설정해주면 됨
            }
        elif response.url.find('naver'):
            yield {
                'sitename': response.url,
                'contents': response.text[:100]
            }
        else:
            yield {
                'sitename': response.url,
                'contents': response.text[:100]
            }
