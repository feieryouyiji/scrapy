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

    