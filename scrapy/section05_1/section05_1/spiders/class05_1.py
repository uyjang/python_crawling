from scrapy.linkextractors import LinkExtractor # 자기가 알아서 1페이지 데이터 가지고 오면 넘기고 2페이지 넘기고 하는 기능
from scrapy.spiders import CrawlSpider, Rule
import re

# https://finance.daum.net/news#economy?page=3
# 링크 크롤링 예제(중요)
# 사이트 요구에 맞는 환경 설정 세팅(중요)
class NewsSpider(CrawlSpider): # 크롤스파이더 사용
    name = 'test11'
    allowed_domains = []
    start_urls = ['https://media.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(정규표현식 사용 추천)
    rules = [
        # page=\d$ or page=\d+$ : 2자리수 페이지 크롤링 2자리수 일 때는 follow=True설정
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_headline'),
    ]

    def parse_headline(self, response):
        print(response)
        # URL 로깅
        # self.logger.info('Response URL : %s' % response.url)

        # for m in response.css('ul.list_news2.list_allnews > li > div'):
        #     # 헤드라인
        #     headline = m.css('strong > a::text').extract_first().strip()
        #     # 본문 20글자
        #     contents = m.css('div > span::text').extract_first().strip()

        #     yield {'headline': headline, 'contents': contents}
