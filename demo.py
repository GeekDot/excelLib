#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from excelLib import ex


# Excel 文件名
file_name = './demo.xlsx'

# 写入 Excel
data = {
        'sheet-1': [[1.1, 1.2, 1.3, 1.4, 1.5], [1.1, 1.2, 1.3, 1.4, 1.5]],
        'sheet-2': [[2.1, 2.2, 2.3, 2.4, 2.5], [2.1, 2.2, 2.3, 2.4, 2.5]],
        'sheet-3': [[3.1, 3.2, 3.3, 3.4, 3.5], [3.1, 3.2, 3.3, 3.4, 3.5]],
    }
ex.write(data, file_name)
print('写入数据:', data)

# 读取 Excel
data = ex.read(file_name)
print('读取数据:', data)
