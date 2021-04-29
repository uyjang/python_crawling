import scrapy


class TestSpider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['https://scrapinghub.com/']
    # 실행은 cmd창에서 scrapy crawl test1
    # 실행은 cmd창에서 section07_2 파일 안의 section07_2 파일 안에 있는 spiders파일 안에 있는 testspider.py를 실행시킬 것이므로 scrapy runspider testspider.py
    # 크롤 실행은 모든 것이 완성된 후 상용화(?)가 됐을 때 실행
    # 런스파이더는 부분 부분 만들면서 국지적으로 실행할 때 (만드는 중간 점검용)
    # --nologs는 cmd창에 로그가 안보이게 함
    
    def parse(self, response): # response에 위의 url홈페이지 갔다오면서 담아온 데이터가 들어감
        # print(response)
        print('dir', dir(response))

        print('status', response.status)

        print('text', response.body)