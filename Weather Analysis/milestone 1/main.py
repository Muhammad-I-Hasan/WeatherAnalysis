import numpy as np
import matplotlib.pyplot as pyplot

from FileIO import *
from TemperatureData import *
from WeatherAnalyzer import *
from Date import *

def main():
    weatherFile = FileIO("CalgaryWeather.csv")
    fileArray = np.array(weatherFile.read_chart())
    TDL = WeatherAnalyzer(fileArray)
    TDL.makeTDlist()
    listmin = []
    listmax = []
    listavgS = []
    choice = 0

    while True:
        print("1- Get Minimum Temperature of 1990-2019")
        print("2- Get Maximum Temperature of 1990-2019")
        print("3- Get Minimum Temperature of 1990-2019 Annually")
        print("4- Get Maximum Temperature of 1990-2019 Annually")
        print("5- Get Average Temperature of 1990-2019 Annually")
        choice = int(input("Choice:"))
        if choice == 1:
            print(f"Minimum Temperature from 1990-2019 is {TDL.getMinTemp()}")
        elif choice == 2:
            print(f"Maximum Temperature from 1990-2019 is {TDL.getMaxTemp()}")
        elif choice == 3:
            listmin = TDL.getMinTempAnnually()
            for i in range(len(listmin)):
                print(f"Year {int(listmin[i][0])} Minimum: {listmin[i][1]}")
        elif choice == 4:
            listmax = TDL.getMaxTempAnnually()
            for i in range(len(listmax)):
                print(f"Year {int(listmax[i][0])} Maximum: {listmax[i][1]}")
        elif choice == 5:
            listavgS = TDL.getAvgSnowFallAnnually()
            for i in range(len(listavgS)):
                print(f"Year {int(listavgS[i][0])} Average Snowfall: {listavgS[i][1]:.3f}")
        elif choice == 0:
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
