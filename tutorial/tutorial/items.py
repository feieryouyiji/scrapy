# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExamItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num = scrapy.Field()
    title = scrapy.Field()
    options = scrapy.Field()


#### 驾校考试
class DrivingExamItem(scrapy.Item):
    """ ['type', 'title', 'option1', 'option2', 'option3', 'option4', 'option5', 'correct_answer', 'score'] """

    num = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    option1 = scrapy.Field()
    option2 = scrapy.Field()
    correct_answer = scrapy.Field()
    score = scrapy.Field()
    

#### 安全消防
class SafeExamItem(scrapy.Item):
    num = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    option1 = scrapy.Field()
    option2 = scrapy.Field()
    option3 = scrapy.Field()
    option4 = scrapy.Field()
    option5 = scrapy.Field()
    correct_answer = scrapy.Field()
    score = scrapy.Field()