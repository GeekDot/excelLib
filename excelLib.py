#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import xlwt
import xlrd


class ExcelLib(object):

    # 写入 Excel
    @staticmethod
    def write(data, file_name):

        # 创建一个工作簿
        workbook = xlwt.Workbook('main')

        # 循环写入每个 sheet 的数据
        for k, v in data.items():

            # 创建工作表
            worksheet = workbook.add_sheet(k)

            # 使用计数器循环写入
            for x in range(len(v)):
                for y in range(len(v[x])):
                    worksheet.write(x, y, v[x][y])

        # 保存 Excel 文件，路径+文件名+后缀名
        workbook.save(file_name)

    # 读取 Excel
    @staticmethod
    def read(file_name):

        # 打开 Excel 文件，路径+文件名+后缀名
        workbook = xlrd.open_workbook(file_name)

        # 获取所有的工作表
        worksheet = workbook.sheets()

        workbook_data = {}

        # 获取工作表
        for sheet in worksheet:

            # 获取当前 sheet 行数
            row = sheet.nrows

            sheet_data = []

            # 获取每行数据，计数器输出每行数据
            for data in range(row):
                row_data = sheet.row_values(data)
                sheet_data.append(row_data)

            workbook_data[sheet.name] = sheet_data

        return workbook_data


ex = ExcelLib()
