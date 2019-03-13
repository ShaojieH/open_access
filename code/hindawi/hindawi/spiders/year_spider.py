import scrapy
from hindawi.items import ArticleItem


class YearSpider(scrapy.Spider):
    name = "year"
    allowed_domains = ["hindawi.com"]
    base_url = "https://www.hindawi.com"
    year = "2018/"
    start_urls = [
        # "https://www.hindawi.com/journals/misy/2018/",
        "https://www.hindawi.com/journals/" 
    ]

    def parse(self, response):
        journals = response.xpath('//ul[@class="li_special"]/li/a/@href').extract()
        journals = [self.base_url + journal + self.year for journal in journals]
        # print(journals)
        for journal_url in journals:
        #journal_url = "https://www.hindawi.com/journals/mpe/2018/"
            print(journal_url)
            yield scrapy.Request(journal_url, callback=self.parse_journal)

    def parse_journal(self, response):
        article_count = 0

        article_count_str = (response.xpath('//span[@class="no_articles"]/text()').extract())[0].split(" ")
        if len(article_count_str) == 18:
            article_count = int(article_count_str[-7].replace(',',''))
        elif len(article_count_str) == 16:
            article_count = int(article_count_str[9].replace("[", ""))
        for i in range(1, int(article_count / 100) + 2):
            page_href = response.url + str(i)
            yield scrapy.Request(page_href, callback=self.parse_list)


    def parse_list(self, response):
        hrefs = response.xpath('//div[@class="middle_content"]/ul/li/a/@href').extract()
        hrefs = ['{0}{1}'.format(self.base_url, href) for href in hrefs]
        for href in hrefs:
            yield scrapy.Request(href, callback=self.parse_article)

    def parse_article(self, response):
        article = ArticleItem()
        article['url'] = response.request.url
        article['title'] = response.xpath('//title/text()').extract()
        article['author_id'] = response.xpath('//span[@class="author"]/a[@class="author_name"]/@data-orcid').extract()
        article['author_affiliation'] = response.xpath('//div[@class="author_gp"]/following-sibling::p[1]/text()').extract()
        article['date'] = response.xpath('//div[@class="author_gp"]/following-sibling::p[3]/text()').extract()[0]
        print(article['url'])
        yield article
