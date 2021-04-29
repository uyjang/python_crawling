import scrapy


class TestSpider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        param: response
        return: title text
        """
        # 아래 4개 다 가능
        # response.css('div.post-header h2 a::text').getall() <-> get() # get은 하나
        # response.css('div.post-header h2 a::text').extract() <-> extract_first() _first는 하나
        # response.xpath('//div[@class="post-header"]/h2/a/text()').getall() <-> get()
        # response.xpath('//div[@class="post-header"]/h2/a/text()').extract() <-> extract_first()

        # 예제1
        # for text in response.css('div.oxy-post-wrap > div > a::text').getall(): # 리스트 형태로 나오기 때문에 for문 돌림
        #     # Return Type : Request, BaseItem, dictionary, None
        #     yield {'text': text}

        # 예제2
        for i, text in enumerate(response.xpath('//div[@class="oxy-post-wrap"]/div/a/text()').getall()):
            # Return Type : Request, BaseItem, dictionary, None
            yield {
                'number': i,
                'text': text
            }

        # 출력 옵션
        # -o 파일명.확장자 -t 파일 타입(json, jsonline, jl, csv, xml, marshal, pickle)
        # scrapy crawl test2 -o result.jl -t jsonline (jl은 제이손 라인이라는 뜻) / -o 뒤에 파일명 쓴 것임


