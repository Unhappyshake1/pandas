import tkinter as tk
from wageCalculator import wageCalculator
from tkinter import filedialog as fd
from tkinter import *

class StartFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Setup Process information
        self.wageCalculator = wageCalculator()
        self.wageCalculator.setProcess('工序名称.xlsx')

        self.Browse_label = Label(self, text='/', bg='white')
        self.Browse_label.place(x=100,y=100)

        self.Browse = Button(self, text='Select a .txt/.csv file', command=lambda: self.file_opener())
        self.Browse.place(x=200,y=200)

    def file_opener(self):

        self.path1 = fd.askopenfilename()
        self.Browse_label = Label(self, text=self.path1, bg='white')
        self.Browse_label.place(x=100,y=100)
        print(self.path1)



        




