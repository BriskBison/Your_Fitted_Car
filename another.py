import pandas
import csv
import matplotlib.pyplot as plt
import numpy as np

class Table():
    def other(self,df):
        self.df = df
        df = pandas.read_csv("cars.csv")
        print(df)

print("Let's see how others chose"))
Table()

class Chart():
    def view(self,y,mylabels):
        self.y = y
        self.mylabels = mylabels
        y = np.array([47, 38, 15])
        mylabels = ["Dodge RAM", "Aston Martin DB12", "Toyota Supra"]
        plt.pie(y, labels = mylabels)
        plt.legend()
        plt.pie(y)
        plt.show()

print("Let's see a chart with people choices")
Chart()
