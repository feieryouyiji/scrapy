#-*- coding:utf-8 -*-
import scrapy
from tutorial.items import DrivingExamItem
from bs4 import BeautifulSoup

class DrivingExamSpider(scrapy.Spider):
    name = "driving_exam"
    allowed_domains = ["wjx.cn"]
    start_urls = [
        
        'https://ks.wjx.top/wjx/join/complete.aspx?q=22253212&JoinID=101440988738&jidx=1&tv=21&s=&hjfb=1',
        'https://ks.wjx.top/jq/22253212.aspx',
    ]
    answer_list = []

    def parse(self, response):
        
        data = response.body
        soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
        if response.url == DrivingExamSpider.start_urls[1]:
            print 'url[0] start~~~'

            for (i, div) in enumerate(soup.find_all('div', class_='div_question')):
                item = DrivingExamItem()
                sub_type = "radio"
                title = unicode(div.find('div', class_='div_title_question'))
                option1 = div.find('label', attrs={"for": 'q%s_1' % str(i+1)}).get_text()
                option2 = div.find('label', attrs={"for": 'q%s_2' % str(i+1)}).get_text()

                # correct_answer_uni = DrivingExamSpider.answer_list[i]
                # print(type(correct_answer_uni), correct_answer_uni, '<unicode???====')

                item.update(
                  num=i,
                  type=sub_type, title=title, 
                  option1=option1, option2=option2,
                  correct_answer=u'正确答案',
                  score=1
                )
                yield item
          

        if response.url == DrivingExamSpider.start_urls[0]:
            print 'url[1] start~~~'
            print len(soup.find_all('div', class_='data__items')), '<====正确答案'
            for (i, div) in enumerate(soup.find_all('div', class_='data__items')):
                div_data_key = div.find('div', class_="data__key")
                text = div_data_key.find('div').get_text()
                DrivingExamSpider.answer_list.append(text)
            
            print(DrivingExamSpider.answer_list, '<===url[1]==================')