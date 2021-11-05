import pandas as pd
import plotly.express as px
import csv
import math

with open("std.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n= len(data)
    sum= 0

    for i in data:
        sum = sum + int(i)

    mean= sum/n
    return mean

squared_list=[]

for i in data:
    a=int(i)-mean(data)
    a=a**2
    squared_list.append(a)

sum= 0
for i in squared_list:
    sum = sum+i

result= sum/(len(data) -1)

stdev=math.sqrt(result)
print(stdev)
