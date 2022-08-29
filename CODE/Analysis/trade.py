import numpy as np
import pandas as pd
from pyecharts.charts import Line
import pyecharts.options as opts

from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.NTERACT
data = pd.DataFrame(pd.read_csv('人民币汇率中间价历史数据.csv',index_col='日期',parse_dates=True,header=0,encoding='gbk'))
data.sort_index(inplace=True)
line = Line(init_opts=opts.InitOpts(width='1600px', height='800px'))
line.add_xaxis(data.index.tolist())  # pyecharts只支持二维列表
line.add_yaxis('汇率', data['USD/CNY'].tolist(), markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_='average')]))
line.set_global_opts(title_opts=opts.TitleOpts(title='美元/人民币汇率'),
                     tooltip_opts=opts.TooltipOpts(
                         is_show=True,
                         trigger='axis',
                         axis_pointer_type='cross'
                     ),
                     xaxis_opts=opts.AxisOpts(
                         type_='category',
                         axispointer_opts=opts.AxisPointerOpts(is_show=True,
                                                               type_='shadow')
                     ),
                     yaxis_opts=opts.AxisOpts(
                         min_='dataMin',
                         axislabel_opts=opts.LabelOpts(formatter='￥{value}')
                     ))

line.render_notebook()
# print(data.head())