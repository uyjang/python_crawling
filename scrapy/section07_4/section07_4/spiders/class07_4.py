import scrapy


class TestSpider(scrapy.Spider):
    # 페이지 순회 크롤링 예제
    name = 'test3'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    # 메인 페이지 순회
    def parse(self, response):
        """
        :param : response
        :return: Request
        """
        # response.css('div.post-item > div > a::attr("href")').getall()
        # response.css('div.post-item > div > a::attr("href")').extract()
        # response.xpath('//div[@class="post-item"]/div/a/@href').getall()
        # response.xpath('//div[@class="post-item"]/div/a/@href').extract()

        for url in response.css('div.oxy-post > a::attr("href")').getall():
            # print(url)
            # url 보다 urljoin 사용 # 이유는 절대경로(https://)로 나오면 상관없겠지만 상대경로(/~)로 나오는 경우에는 조인을 사용해야한다.자동으로 위의 start url 변수를 붙여줌
            yield scrapy.Request(response.urljoin(url), self.parse_title) # 여기서 요청된 url을 처리해주는 함수는 self.parse_title이다.

    # 상세 페이지 순회
    def parse_title(self, response): # 위에서 url을 통해서 가져온 데이터들(blog 뜬 갯수만큼)이 전부 실행됨(반복함)
        """
        상세 페이지 -> 타이틀 추출
        :param response: 
        :return Contents Text :
        """
        contents = response.css('div#blog-body > span > p::text').getall()[:5]
        # print(contents)
        yield {'contents': ''.join(contents)} # contents 다음에 빈공간 없이 바로 컨텐츠(본문내용)이 붙음.
