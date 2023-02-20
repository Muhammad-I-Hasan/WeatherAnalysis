import numpy as np
import matplotlib.pyplot as pyplot

from FileIO import *
from TemperatureData import *
from WeatherAnalyzer import *
from Date import *

class Chart:
    def drawLineChart(self,x,y,title,xlabel,ylabel):
        fig = pyplot.figure()
        pyplot.title(title)
        pyplot.ylabel(ylabel)
        pyplot.xlabel(xlabel)
        pyplot.plot(x,y,marker='o')
        pyplot.show()
    def drawBarChart(self,x,y,title,xlabel,ylabel):
        y_pos = np.arange(len(x))
        performance = x
        pyplot.bar(y_pos, performance, align='center', alpha=0.5)
        pyplot.xticks(y_pos, x)
        pyplot.ylabel(ylabel)
        pyplot.title(title)
        pyplot.show()
