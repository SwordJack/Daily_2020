# -*- coding: utf-8 -*-
# ./usr/bin/env python
'''
Bar效果演示图。

@version: N/A
@interpretor: python37_64
@source: http://gallery.pyecharts.org/#/Bar/bar_base_dict_config
'''

from pyecharts.charts import Bar
from pyecharts.faker import Faker   # Faker是pyecharts的一个伪数据生成器。
from pyecharts.globals import ThemeType

c = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts={"text": "Bar-通过 dict 进行配置", "subtext": "我也是通过 dict 进行配置的"}  # 标题和副标题可以通过字典类型进行配置。
    )
    .render("{}.html".format(__file__))
)
