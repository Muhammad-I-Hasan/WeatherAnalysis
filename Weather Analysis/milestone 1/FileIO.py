import numpy as np
import matplotlib.pyplot as pyplot

class FileIO:
    def __init__(self,file_name):
        self.file_name = file_name
    def read_chart(self):
        data = np.loadtxt(self.file_name, delimiter=',', skiprows=1, usecols=(0,1,2,3,4), dtype=np.float)
        return data