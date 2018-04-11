# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import xlsxwriter


def write_sheet_row(workbook, sheet, row_value_list, row_index, is_bold):
        print row_index, '**************'
        i = 0
        cell_format = workbook.add_format({'bold': is_bold, 'font_color': 'black'})
        for s_value in row_value_list:
            sheet.write(row_index, i, s_value, cell_format)
            i = i + 1



class DrivingExamPipeline(object):
    temp_path = r'/home/demlution/Desktop/scrapy/tutorial/temp_file/driving_exam11.xls'
    head_list = [u'题型', u'题目内容', u'选项A', u'选项B', u'选项C', u'选项D', u'选项E', u'正确选项', u'分值']

    workbook = xlsxwriter.Workbook(temp_path)
    sheet = workbook.add_worksheet(u'选择')
    write_sheet_row(workbook, sheet, head_list, 0, True)

    def process_item(self, item, spider):
        print item, '<======item'
        print type(item['correct_answer']), '<======item'
        print item['correct_answer'], '<====print==item'
        print item['correct_answer'][7:9], '<==798==print==item'
        print item['correct_answer'][8:10], '<====print==item'

        value_list = [ 
                u'单选', 
                item.get('title'),
                item.get('option1'),
                item.get('option2'),
                u'',
                u'',
                u'',
                u'A' if item['correct_answer'][7:9] == u'正确' else u'B',
                1,
        ]
        write_sheet_row(DrivingExamPipeline.workbook, DrivingExamPipeline.sheet, value_list, item['num']+1, False )

        # self.write_sheet_row(workbook, sheet, value_list, item.get('num')+1, False)  # 写入每一行
        if item['num'] == 39:
            DrivingExamPipeline.workbook.close()
        return item


# 房产测评pipeline
class EvaluationPipeline(object):
    def __init__(self):
        self.temp_path = r'/home/demlution/Desktop/scrapy/tutorial/temp_file/evaluation_xinli.xls'
        self.head_list = [u'题型', u'题目描述', u'选项A', u'选项B', u'选项C', u'选项D', u'选项E', u'选项A分值', u'选项B分值', u'选项C分值', u'选项D分值', u'选项E分值']
        self.workbook = xlsxwriter.Workbook(self.temp_path)
        self.sheet = self.workbook.add_worksheet(u'单选题')
        write_sheet_row(self.workbook, self.sheet, self.head_list, 0, True)

    def process_item(self, item, spider):
        value_list = [
                u'单选', 
                item.get('title'),
                item.get('option1'),
                item.get('option2'),
                item.get('option3'),
                item.get('option4'),
                item.get('option5'),
                item.get('score1'),
                item.get('score2'),
                item.get('score3'),
                item.get('score4'),
                item.get('score5')
        ]
        write_sheet_row(self.workbook, self.sheet, value_list, item['num'] + 1, False)

    # 处理结束后关闭 文件 IO 流
    def close_spider(self, spider):
        self.workbook.close()