<h2 align= center> excelLib Excel 处理库 </h2>

<h5 align=right> 张懿 </h5>
<p align=right> 2019-09-11 </p>

### 一、概述

`excelLib` 是 Excel 处理库，依赖 `xlwt`、`xlrd` 库，`excelLib` 是对 `xlwt`、`xlrd` 库进行二次封装，使用更加方便简洁，只用一行就可以解决绝大部分的问题

下面是对 `excelLib` 的详解，如想快速使用，请移步 `demo.py` 模块，里面有 `excelLib` 的使用 `demo`

### 二、安装

`excelLib` 是以源码的方式呈现，使用的时候直接导入即可

	from excelLib import ex
    
### 三、使用

`excelLib` 提供了两个方法：`read`和 `write`

`read`：需要传入 `1` 个必要参数 `file_name`，`file_name` 是文件名称（路径+文件名+后缀名）。返回值是字典类型的，字典的 `key` 是按顺序输出的每一个 `sheet`，`value` 是一个二维数组，分别代表每个 `sheet` 中的行和列

`write`：需要传入 `2` 个必要参数，`data`、`file_name`，`file_name` 是文件名称（路径+文件名+后缀名），`data` 是要写入的数据， `data` 是一个字典类型的，字典的 `key` 是 `Excel` 中的 `sheet`，`value` 是一个二维数组，分别代表每个 `sheet` 中的行和列，二维数组必须保证行数一致，如果数据为空赋值为空字符串即可

    # Excel 文件名
    file_name = './demo.xlsx'
    
    # 写入 Excel
    data = {
            'sheet-1': [[1.1, 1.2, 1.3, 1.4, 1.5], [1.1, 1.2, 1.3, 1.4, 1.5]],
            'sheet-2': [[2.1, 2.2, 2.3, 2.4, 2.5], [2.1, 2.2, 2.3, 2.4, 2.5]],
            'sheet-3': [[3.1, 3.2, 3.3, 3.4, 3.5], [3.1, 3.2, 3.3, 3.4, 3.5]],
        }
    ex.write(data, file_name)
    
    # 读取 Excel
    data = ex.read(file_name)
    print(data)

执行结果：

    {'sheet-1': [[1.1, 1.2, 1.3, 1.4, 1.5], [1.1, 1.2, 1.3, 1.4, 1.5]], 'sheet-2': [[2.1, 2.2, 2.3, 2.4, 2.5], [2.1, 2.2, 2.3, 2.4, 2.5]], 'sheet-3': [[3.1, 3.2, 3.3, 3.4, 3.5], [3.1, 3.2, 3.3, 3.4, 3.5]]}
