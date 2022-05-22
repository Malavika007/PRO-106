import numpy as np
import pandas as pd
import csv
import plotly.express as px

def plot_figure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = 'Days Present', y = 'Marks In Percentage')
        fig.show()

def getDataSource(data_path):
    student_marks = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            student_marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    
    return {"x":student_marks, "y":days_present}

def findCorelation(data_source):
    corelation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between student marks and days present  :-  \n--->",corelation[0,1])

data_path = "Student Marks vs Days Present.csv"
data_source = getDataSource(data_path)
findCorelation(data_source)
plot_figure(data_path)