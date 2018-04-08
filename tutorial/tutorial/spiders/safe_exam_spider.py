#-*- coding:utf-8 -*-
import scrapy
from tutorial.items import SafeExamItem
from bs4 import BeautifulSoup
import re

class SafeExamSpider(scrapy.Spider):
    name = "safe_exam"
    allowed_domains = ["wjx.cn"]
    start_urls = [
        'https://ks.wjx.top/wjx/join/complete.aspx?q=22274266&JoinID=101447010367&jidx=1&tv=45&s=&hjfb=1',
        'https://ks.wjx.top/jq/22274266.aspx',
    ]
    answer_list = []

    def parse(self, response):
        
        data = response.body
        soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
        if response.url == SafeExamSpider.start_urls[1]:
            for (index, div) in enumerate(soup.find_all('div', class_='div_question')):
                item = SafeExamItem()
                sub_type = "radio" if index <= 11 else 'checkBox'
                title = unicode(div.find('div', class_='div_title_question'))
                options = [opt.get_text() for opt in div.find_all('label')]
                new_opts = []
                for x in options:
                    limituni = ur"[A|B|C|D|E]、"
                    new_x = re.sub(limituni, '', x)
                    print new_x, 'nexxxxx'
                    new_opts.append(new_x)
                for i in range(5):
                    opt_key = 'option%s' % (i+1)
                    if i <= len(new_opts)-1:
                        item[opt_key] = new_opts[i]
                    else:
                        item[opt_key] = ''

                # correct_answer_uni = DrivingExamSpider.answer_list[i]
                print(index, 'i<=========')
                item.update(
                  num=index,
                  type=sub_type, title=title, 
                  correct_answer='',
                  score=1
                )
                yield item
          
        if response.url == SafeExamSpider.start_urls[0]:
            print '<><><><><><><><><><><><'
            print 'lens==>', len(soup.find('div', class_='query__data-result').find_all('div', class_='data__items'))
            for (i, div) in enumerate(soup.find_all('div', class_='data__items')):
                new_dict = {}
                div_title = div.find('div', class_='data__tit')
                
                # score_uni = div_title.find('span')
                print(div, 'div_title<-======')
              
                return
                div_data_key = div.find('div', class_="data__key")
                text = div_data_key.find('div').get_text()
                SafeExamSpider.answer_list.append(text)
            
            print(SafeExamSpider.answer_list, '<===url[1]==================')