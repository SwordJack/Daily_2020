# -*- coding: utf-8 -*-
# ./usr/bin/env python
'''
尝试绘制echarts中国地理信息绘图。

@version: N/A
@interpretor: python37_64
@author: Zhong Y. Jie
@modification_date: 2020.04.18
'''

import numpy as np
import pandas as pd
import json
from pandas.io.json import json_normalize
from collections import Counter

from pyecharts.charts import Geo
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType

g0 = (
    Geo()
    .add_schema(maptype='china')
    .add('geo', [list(z) for z in zip(Faker.provinces, Faker.values())])
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False)    # 不显示省份对应数值的标签。
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(          # 显示左下角的色条和图上的色彩渐变。
            is_piecewise=True,      # 设置为分段显示。
            max_=200,               # 设置色条上限。
            split_number=10,        # 设置分段数目。
            ),
        title_opts=opts.TitleOpts(title="geo_china"),
    )
)
g0.render('{}.html'.format(__file__))
