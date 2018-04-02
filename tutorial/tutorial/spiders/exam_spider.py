import scrapy
from tutorial.items import ExamItem
from bs4 import BeautifulSoup  


class ExamSpider(scrapy.Spider):
    name = "exam"
    allowed_domains = ["wjx.cn"]
    start_urls = [
        'https://www.wjx.cn/jq/401525.aspx'
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        print 'hahahhaha===>>>>>'
        data = response.body
        
        soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
        print len(soup.find_all('div', class_='div_question')), '<====len'
        for div in soup.find_all('div', class_='div_question'):
            item = ExamItem()
            num = div.find('div', class_='div_topic_question').get_text()
            title = div.find('div', class_='div_title_question').get_text()
            bs_lis = div.find('div', class_='div_table_radio_question').find_all('li')
            options = [li.find('label').get_text() for li in bs_lis]
            item.update(num=num, title=title, options=options)
            yield item