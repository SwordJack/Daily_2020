# -*- coding: utf-8 -*-
# ./usr/bin/env python
'''
尝试绘制echarts条形图。

@version: N/A
@interpretor: python37_64
@author: Zhong Y. Jie
@modification_date: 2020.04.17
'''

from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

month_columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]  # 设置行名

data_precipitation = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]  # 设置降水量数据。
data_evaporation = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]    # 设置蒸发量数据。

bar = Bar(
    init_opts=opts.InitOpts(theme=ThemeType.ESSOS)  # 配置图形主题。
)
bar.add_xaxis(month_columns)
bar.add_yaxis(
    '降水量',                                  # 设置系列名。
    data_precipitation,                        # 配置数据源。
    itemstyle_opts=opts.ItemStyleOpts(         # 配置图形。
        color='CornFlowerBlue'
        )
    )
bar.add_yaxis('蒸发量', data_evaporation)
bar.set_global_opts(
    title_opts=opts.TitleOpts(                      # 设置标题和副标题，或用字典形式也可。
        title='条形图示例',
        subtitle='降水量、蒸发量显示'
        ),
    datazoom_opts=opts.DataZoomOpts(is_show=True),  # 设置显示滚动条。
    yaxis_opts=opts.AxisOpts(max_=200),             # 配置y轴最大值为200，类似方法可配置x轴。
    toolbox_opts=opts.ToolboxOpts(),                # 配置工具箱栏。
)

bar.set_series_opts(
    label_opts=opts.LabelOpts(is_show=False),       # 设置在图表上显示具体数值，默认为True，此处设置为不显示。
    markpoint_opts=opts.MarkAreaOpts(               # 设置显示数据标记点。
        data=[
            opts.MarkPointItem(type_='max'),        # 标记最大值点。
            opts.MarkPointItem(type_='min'),        # 标记最小值点。
        ]
    ),
    markline_opts=opts.MarkLineOpts(                # 设置显示数据标记线。
        data=[
            opts.MarkLineItem(type_='average', name='平均') # 标记平均值线和线名称，线名称会在鼠标浮于其上时显示。
        ]
    )
)


bar.render('{}.html'.format(__file__))
