import pandas as pd
import numpy as np
import tkinter as tk


class wageCalculator:

    def __init__(self):
        self.product = []
        self.group = []
        self.key = []
        self.prices = []
        self.names = []


    def setProcess(self,process_path):
        # Read the Excel
        df_process = pd.read_excel(process_path)

        # Convert the data to numpy Array
        self.process_array = df_process.to_numpy()



    def setProduct(self):
        for i in range(len(self.process_array)):
            for j in range(len(self.process_array[0])):
                if str(self.process_array[i][0]) not in str(self.product):
                    self.product.append(str(self.process_array[i][0]))

    def setGroup(self):
        for i in range(len(self.process_array)):
            for j in range(len(self.process_array[0])):
                if str(self.process_array[i][1]) not in str(self.group):
                    self.group.append(str(self.process_array[i][1]))

    def setDict(self):
        for i in range(len(self.process_array)):
            for j in range(len(self.process_array[0])):
                if ( str(self.process_array[i][0]) + str(self.process_array[i][1]) + str(self.process_array[i][2])) not in str(self.key):
                    self.key.append(str(str(self.process_array[i][0]) + str(self.process_array[i][1])) + str(self.process_array[i][2]))
                    self.names.append(self.process_array[i][3])
                    self.prices.append(self.process_array[i][4])
        self.dict = {self.key[i] : (self.names[i],self.prices[i]) for i in range (len(self.key))}

    def test(self):
        self.setProduct()
        self.setGroup()
        self.setDict()
        print(self.dict)

