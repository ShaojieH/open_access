import json
import codecs
from lxml import etree
data_path = "../../data/"
usnews_ranking_2019_path = data_path + "ranking/usnews_ranking_2019.html"
# data retried on 2019/3/13
def main():
    with open(usnews_ranking_2019_path,"r") as f:
        html = f.read()
        tree=etree.HTML(html)
        nodes = tree.xpath("//tr[@data-view='colleges-search-results-table-row']/td[@class='full-width']")
        names = [node.xpath("//div[@class='text-strong text-large block-tighter']/a/text()") for node in nodes]
        rankings = [node.xpath("//div[@class='text-small']/span/text()") for node in nodes]
        #print(names, rankings)
        print(len(names), len(rankings))
        #nodes.xpath("//div[@class='text-strong text-large block-tighter']")
if __name__ == "__main__":
    main()