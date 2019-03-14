
import scrapy
from ranking.items import RankingItem
class UsNews(scrapy.Spider):
    name = "usnews"
    allowed_domains = ["usnews.com"]

    start_urls = [
        ("https://www.usnews.com/education/best-global-universities/search?country=united-states&page=" + str(i)) for i in range(1, 26)
        #start_url
    ]

    def parse(self, response):
        print(response)
        names = response.xpath("//div[@class='sep']/div[@class='block unwrap']/h2/a/text()").extract()
        rankings = [int(ranking.replace('\n','').strip().replace('#', '')) for ranking in response.xpath("//div[@class='sep']/div[contains(@class,'thumb-left')]/span/text()").extract() if '#' in ranking]
        item = RankingItem()
        for name, ranking in zip(names, rankings):
            item['name'] = name
            item['ranking'] = ranking
            yield item
