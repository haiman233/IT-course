# -*- coding: utf-8 -*-

import numpy as np  #引入numpy库模块，用np替代
import matplotlib.pyplot as plt  #引入matplotlib库模块中的pyplot方法，用plt替代
from pylab import *   #引入pylab库模块中的所有方法
x = np.arange(-5.0, 5.0, 0.02)   #定义x轴数值为-5到5，步长为0.02
y = np.sin(x)   #利用正弦函数计算出x轴数值对应的y轴数值你
plt.plot(x, y)    #利用x,y轴对应的数值绘制出图形
plt.show()   #显示出绘制的图形

 