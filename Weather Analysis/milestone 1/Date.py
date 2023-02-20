import numpy as np
import matplotlib.pyplot as pyplot

class Date:
    def __init__(self,year,month):
        self.month = month
        self.year = year
    def getmonth(self):
        return self.month
    def getyear(self):
        return self.year