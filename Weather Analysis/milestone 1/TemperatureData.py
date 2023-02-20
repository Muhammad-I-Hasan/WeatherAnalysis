import numpy as np
import matplotlib.pyplot as pyplot

class TemperatureData:
    def __init__(self,Date,max,min,snow):
        self.Date = Date
        self.min = min
        self.max = max
        self.snow = snow
    def getmin(self):
        return self.min
    def getmax(self):
        return self.max
    def getsnow(self):
        return self.snow