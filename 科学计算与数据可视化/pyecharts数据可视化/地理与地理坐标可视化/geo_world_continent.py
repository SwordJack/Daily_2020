# -*- coding: utf-8 -*-
# ./usr/bin/env python
'''
尝试绘制echarts世界地理信息绘图。

地图被分为NA（北美）、EMEA（欧洲、中东、非洲）、AP（亚太）、CALA（加勒比海、拉丁美洲）四部分。
    NA取美国芝加哥的经纬度（经度在前，纬度在后）；
    EMEA，取意大利首都罗马的经纬度；
    AP取中国上海的经纬度；
    CALA取委内瑞拉首都加拉加斯的经纬度；

@version: N/A
@interpretor: python37_64
@author: Zhong Y. Jie
@modification_date: 2020.04.18
'''

from os import getcwd   # 获取文件当前目录。
import numpy as np
import pandas as pd
import json
from pandas.io.json import json_normalize
from collections import Counter

from pyecharts.charts import Geo
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType
from pyecharts.globals import ThemeType, GeoType, ChartType

g0 = (
    Geo(
        init_opts=opts.InitOpts(
            theme=ThemeType.MACARONS,   # 设置图表主题。
            width='100vw',             # 设置图表宽度。
            height='100vh',             # 设置图表高度。
            )
    )
    .add_schema(maptype='world')            # 使用世界地图。
    .add_coordinate_json('{}\\{}'.format(getcwd(), 'continent_position.json'))
)

data_pair = [   # 为各大洲赋给数值。
    ['NA', 23.640],
    ['EMEA', 25.573],
    ['AP', 58.949],
    ['CALA', 5.403],
]

g0.add('geo',
    data_pair,
    type_=GeoType.EFFECT_SCATTER,   # 可产生涟漪效果。
    symbol_size=10
)
g0.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(          # 显示左下角的色条和图上的色彩渐变。
            is_piecewise=False,     # 设置为连续显示。
            max_=60,                # 设置色条上限。
            split_number=6,         # 设置分段数目。
            ),
        title_opts=opts.TitleOpts(title="全球无线网络市场空间"),
        toolbox_opts=opts.ToolboxOpts(),
    )

g0.render('{}.html'.format(__file__))
