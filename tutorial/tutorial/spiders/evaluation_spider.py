#-*- coding:utf-8 -*-
import scrapy
from tutorial.items import EvaluationItem
from bs4 import BeautifulSoup
import re


class EvaluationSpider(scrapy.Spider):
    name = "evaluation"
    allowed_domains = ["wjx.cn"]
    start_urls = [
        # 'https://www.wjx.cn/jq/22375322.aspx',  # 房产测评试卷
        'https://www.wjx.cn/jq/22420692.aspx',  # 心理健康症状自评量表SCL-90  
    ]
    
    def parse(self, response):
        
        data = response.body
        soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')

        for (index, div) in enumerate(soup.find_all('div', class_='div_question')):
            item = EvaluationItem()

            limit_title_uni1 = ur'<span class="req">\xa0\*</span>'
            limit_title_uni2 = ur'\d+\.'
            title = unicode(div.find('div', class_='div_title_question'))
            title = re.sub(limit_title_uni1, '', title)
            title = re.sub(limit_title_uni2, '', title)
            print(div.find_all('label'), ' title<===')
            options = [
              opt.get_text()
              for (i, opt) in enumerate(div.find_all('label'))
            ]
            print(options, 'opt<===')
            new_opts = []
            for x in options:
                limituni = ur"[A|B|C|D|E]\."
                new_x = re.sub(limituni, '', x)
                new_opts.append(new_x)
            for i in range(5):
                opt_key = 'option%s' % (i+1)
                score_key = 'score%s' % (i+1)
                if i <= len(new_opts)-1:
                    item[opt_key] = new_opts[i]
                    item[score_key] = i + 1
                else:
                    item[opt_key] = ''
                    item[score_key] = ''
                
            item.update(
              num=index,
              type='radio', title=title, 
            )
            yield item
