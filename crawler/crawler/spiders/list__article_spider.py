import scrapy
from crawler.items import Article

class ListArticleSpider(scrapy.Spider):
    name = "list_article"
    allowed_domains = ["arxiv.org"]
    start_urls = [
        "https://arxiv.org/list/cs.AI/pastweek?skip=57&show=25",
    ]

    def parse(self, response):
        for sel in response.xpath('//dd/div'):
            item = Article()
            item['title'] = sel.xpath('div[@class="list-title mathjax"]/text()').extract()[1].strip().encode('utf-8').decode("utf-8")
            item['authors'] = [author.encode('utf-8').decode("utf-8") for author in sel.xpath('div[@class="list-authors"]/a/text()').extract()]
            item['id'] = sel.xpath('../preceding-sibling::*[1]/span/a[@title="Abstract"]/text()').extract()[0].replace("arXiv:", "").encode('utf-8').decode("utf-8")
            yield item

