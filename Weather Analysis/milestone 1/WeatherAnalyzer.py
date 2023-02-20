import numpy as np
import matplotlib.pyplot as pyplot

from Date import *
from TemperatureData import *

class WeatherAnalyzer:
    def __init__(self,a):
        self.a = a
        self.TDlist = []

    def makeTDlist(self):
        for i in range(359):
            tempD = Date(self.a[i][0],self.a[i][1])
            tempTD = TemperatureData(tempD,self.a[i][2],self.a[i][3],self.a[i][4])
            self.TDlist.append(tempTD)
    
    def getMinTemp(self):
        min = 0
        for i in range(len(self.TDlist)):
            if i == 0:
                min = self.TDlist[i].getmin()
            elif i != 0 and self.TDlist[i].getmin() < min:
                min = self.TDlist[i].getmin()
        return min

    def getMinTempAnnually(self):
        temparr = []
        minarr = []
        x = 0
        for i in range(1990,2021):
            for j in range(x,len(self.TDlist)):
                if self.TDlist[j].Date.getyear() == i:
                    temparr.append(self.TDlist[j].getmin())
                elif self.TDlist[j].Date.getyear() != i:
                    minarr.append(np.min(temparr))
                    #@print(temparr) 
                    temparr.clear()
                    x = j
                    break
        #print(minarr)
        temparray = np.zeros((30,2))
        temp = np.arange(1990,2020)
        temparray[:,0] = temp
        temparray[:,1] = minarr
        listmin = temparray.tolist()
        #print(list1)
        return listmin

    def getMaxTemp(self):
        max = 0
        for i in range(len(self.TDlist)):
            if i == 0:
                max = self.TDlist[i].getmax()
            elif i != 0 and self.TDlist[i].getmax() > max:
                max = self.TDlist[i].getmax()
        return max

    def getMaxTempAnnually(self):
        temparr = []
        maxarr = []
        x = 0
        for i in range(1990,2021):
            for j in range(x,len(self.TDlist)):
                if self.TDlist[j].Date.getyear() == i:
                    temparr.append(self.TDlist[j].getmax())
                elif self.TDlist[j].Date.getyear() != i:
                    maxarr.append(np.max(temparr))
                    #print(temparr) 
                    temparr.clear()
                    x = j
                    break
        #print(maxarr)
        temparray = np.zeros((30,2))
        temp = np.arange(1990,2020)
        temparray[:,0] = temp
        temparray[:,1] = maxarr
        listmax = temparray.tolist()
        #print(list1)
        return listmax

    def getAvgSnowFallAnnually(self):
        temparr = []
        avgarr = []
        x = 0
        for i in range(1990,2021):
            for j in range(x,len(self.TDlist)):
                if self.TDlist[j].Date.getyear() == i:
                    temparr.append(self.TDlist[j].getsnow())
                elif self.TDlist[j].Date.getyear() != i:
                    avgarr.append(np.average(temparr))
                    #print(temparr) 
                    temparr.clear()
                    x = j
                    break
        #print(avgarr)
        temparray = np.zeros((30,2))
        temp = np.arange(1990,2020)
        temparray[:,0] = temp
        temparray[:,1] = avgarr
        listavg = temparray.tolist()
        #print(list1)
        return listavg

    #def getAvgTempAnnually(self):
