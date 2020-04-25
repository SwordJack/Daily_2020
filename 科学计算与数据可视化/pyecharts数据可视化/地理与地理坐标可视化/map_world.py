# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
尝试绘制echarts下map的世界地图绘图。

@file                : map_world.py
@version             : N/A
@interpretor         : python37_64
@modification_date   : 2020.04.21
@author              : Zhong Y. Jie
'''

from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

country_total_pair = [['United States', 20.488000000000003], ['France', 32.408], ['China', 27.531999999999996], ['Brazil', 4.067]]
print(country_total_pair)
# c = (
#     Map()
#     .add("商家A", country_value_pair, "world")
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="Map-world"), visualmap_opts=opts.VisualMapOpts()
#     )
#     .render("map_world.html")
# )
map_chart = (
        Map(
            # init_opts=opts.InitOpts(
            #     theme=ThemeType.MACARONS,   # 设置图表主题。
            #     width='98vw',               # 设置图表宽度。
            #     height='98vh',              # 设置图表高度。
            # )
        )
        .add(
            series_name='total',            # 序列名
            data_pair=country_total_pair,   # 数据源（待修改）
            maptype='world',                # 地图类型
            is_roam=False,                  # 地图不可拖动
            is_map_symbol_show=False,       # 不显示标记图形
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                '{}年第{}季度无线网络市场'.format(
                    2001, 1
                ),
            ),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
map_chart.render('map_world.html')
