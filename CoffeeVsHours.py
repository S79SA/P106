import plotly_express as px
import csv

import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x = "Amount", y = "Time")
        fig.show()

def getDataSource(data_path):
    coffee = []
    hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        coffee.append(float(row["Amount"]))
        hours.append(float(row["Time"]))

    return{"x": time, "y":amount}


