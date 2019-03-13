import scrapy
from crawler.items import Article

class ArticleSpider(scrapy.Spider):
    name = "article"
    allowed_domains = ["arxiv.org"]
    start_urls = [
        "https://arxiv.org/abs/1810.11370",
        "https://arxiv.org/abs/1810.09661"
    ]

    def parse(self, response):
        item = Article()
        item['title'] = response.xpath('//h1[@class="title mathjax"]/text()').extract()[0].encode('utf-8').decode("utf-8")
        item['authors'] = [author.encode('utf-8').decode("utf-8") for author in response.xpath('//div[@class="authors"]/a//text()').extract()]
        item['link'] = response.url
        item['id'] = response.xpath('//meta[@name="citation_arxiv_id"]/@content').extract()[0]
        item['date'] = response.xpath('//div[@class="dateline"]/text()').extract()[0]
        yield item

