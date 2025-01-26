import pandas
import csv

class Table():
    def other(self,df):
        self.df = df

        print("Let's how other people have chosen")
        df = pandas.read_csv("cars.csv")
        print(df)

Table()

import matplotlib.pyplot as plt
import numpy as np

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

Chart()


# """ TODO 5  Enumerate, enum, dekoratory sortowanie, lambdę  oraz generatory można użyć w
#       trakcie pisania informacji technicznych na temat samochodu, który został wybrany """
# """ TODO 6 Wszystkie kolejne rzeczy których się dowiem mogą być użyte przy porównywaniu
#            samochodów i ich osiągów""