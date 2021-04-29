import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import ArticleItems


# 페이지 + 상세 페이지 크롤링 추가
# 미들웨어 설치 : pip install scrapy_fake_useragent
class NewsSpider(CrawlSpider):
    name = 'test12'
    # 허용 도메인
    allowed_domains = []
    # 시작 URL(2페이지로 변경)
    start_urls = ['https://media.daum.net/breakingnews/digital']

    rules = [
        # 뉴스 메인페이지
        # 테스트 시 : page=\d$ 수정
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_parent'),
    ]

    def parse_parent(self, response):
        # 부모 상세 URL 로깅
        self.logger.info('Parent Response URL : %s' % response.url)

        # 페이지내 신문 상세 요청
        for url in response.css('ul.list_news2.list_allnews > li > div'):
            # 신문 기사 URL
            article_url = url.css('strong > a::attr(href)').extract_first().strip() # 부모 페이지?에서 헤드라인들만 긁어 온것이고
            # 요청
            yield scrapy.Request(article_url, self.parse_child, meta={'parent_url': response.url}) # 자식에게 부모페이지url 정보를 넘겨주고 자식은 그 정보를 바탕으로 헤드라인에 해당되는 기사를 분석함

    def parse_child(self, response):
        # 부모, 자식 수신 정보 로깅
        self.logger.info('-------------------------------------------')
        self.logger.info('Response From Parent URL : %s' % response.meta['parent_url'])
        self.logger.info('Child Response URL : %s' % response.url) # article_url의 url이 들어온 것임
        self.logger.info('Child Response Status : %s' % response.status)
        self.logger.info('-------------------------------------------')
        pass
        # # 헤드라인
        headline = response.css('h3.tit_view::text').extract_first().strip()
        # # 본문 20글자
        c_list = response.css('div.article_view p::text').extract_first().strip()
        # # 리스트 -> 문자열 변경
        contents = ''.join(c_list).strip()

        yield ArticleItems(headline=headline, contents=contents,
                           parent_link=response.meta['parent_url'],
                           article_link=response.url)
