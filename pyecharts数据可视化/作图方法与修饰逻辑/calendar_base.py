# -*- coding: utf-8 -*-
# ./usr/bin/env python
'''
Calendar效果演示图。

@version: N/A
@interpretor: python37_64
@source: http://gallery.pyecharts.org/#/Calendar/calendar_base
'''

import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar


begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]

c = (
    Calendar()      # 各类型图表可以进行链式调用。
    .add("", data, calendar_opts=opts.CalendarOpts(range_="2017"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Calendar-2017年微信步数情况"),
        visualmap_opts=opts.VisualMapOpts(
            max_=20000,
            min_=500,
            orient="horizontal",
            is_piecewise=True,
            pos_top="230px",
            pos_left="100px",
        ),
    )
    .render("{}.html".format(__file__))
)
