import pandas as pd
import numpy as np
import random
from collections import defaultdict

from random import randint
from datetime import datetime, timedelta

from jchart import Chart
from jchart.config import Axes, DataSet, rgba

# Importing data
df = pd.read_csv('data.csv')

# Bar Chart
bar_chart_x_labels = list(set(df['ShopName']))
bar_chart_y_labels = []
bar_chart_colors = []
for i in range(len(bar_chart_x_labels)):
    bar_chart_colors.append(rgba((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)),5  ))    
x = defaultdict(lambda:0)
for ind in df.index:
    x[df['ShopName'][ind]]+=int(df['Quantity'][ind])
for i in bar_chart_x_labels:
    bar_chart_y_labels.append(x[i])



class TimeSeriesChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Axes(type='time', position='bottom')],
    }

    def get_datasets(self, *args, **kwargs):
        data = [{'y': 0, 'x': '2017-01-02T00:00:00'}, {'y': 1, 'x': '2017-01-03T00:00:00'}, {'y': 4, 'x': '2017-01-04T00:00:00'}, {'y': 9, 'x': '2017-01-05T00:00:00'}, {'y': 16, 'x': '2017-01-06T00:00:00'}, {'y': 25, 'x': '2017-01-07T00:00:00'}, {'y': 36, 'x': '2017-01-08T00:00:00'}, {'y': 49, 'x': '2017-01-09T00:00:00'}, {'y': 64, 'x': '2017-01-10T00:00:00'}, {'y': 81, 'x': '2017-01-11T00:00:00'}, {'y': 100, 'x': '2017-01-12T00:00:00'}, {'y': 121, 'x': '2017-01-13T00:00:00'}, {'y': 144, 'x': '2017-01-14T00:00:00'}, {'y': 169, 'x': '2017-01-15T00:00:00'}, {'y': 196, 'x': '2017-01-16T00:00:00'}, {'y': 225, 'x': '2017-01-17T00:00:00'}, {'y': 256, 'x': '2017-01-18T00:00:00'}, {'y': 289, 'x': '2017-01-19T00:00:00'}, {'y': 324, 'x': '2017-01-20T00:00:00'}, {'y': 361, 'x': '2017-01-21T00:00:00'}, {'y': 400, 'x': '2017-01-22T00:00:00'}, {'y': 441, 'x': '2017-01-23T00:00:00'}, {'y': 484, 'x': '2017-01-24T00:00:00'}, {'y': 529, 'x': '2017-01-25T00:00:00'}, {'y': 576, 'x': '2017-01-26T00:00:00'}, {'y': 625, 'x': '2017-01-27T00:00:00'}, {'y': 676, 'x': '2017-01-28T00:00:00'}, {'y': 729, 'x': '2017-01-29T00:00:00'}, {'y': 784, 'x': '2017-01-30T00:00:00'}, {'y': 841, 'x': '2017-01-31T00:00:00'}, {'y': 900, 'x': '2017-02-01T00:00:00'}]

        return [DataSet(
            type='line',
            label='Time Series',
            data=data,
        )]


class ScatterLineChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Axes(type='time', position='bottom')],
    }

    def get_datasets(self, **kwargs):
        data_scatter = [{'y': 24, 'x': '2017-01-01T21:00:00'}, {'y': 1, 'x': '2017-01-02T03:00:00'}, {'y': 7, 'x': '2017-01-02T14:00:00'}, {'y': 7, 'x': '2017-01-03T08:00:00'}, {'y': 13, 'x': '2017-01-04T00:00:00'}, {'y': 7, 'x': '2017-01-04T07:00:00'}, {'y': 19, 'x': '2017-01-05T01:00:00'}, {'y': 18, 'x': '2017-01-05T15:00:00'}, {'y': 14, 'x': '2017-01-06T00:00:00'}, {'y': 2, 'x': '2017-01-06T07:00:00'}, {'y': 18, 'x': '2017-01-07T06:00:00'}, {'y': 4, 'x': '2017-01-07T07:00:00'}, {'y': 21, 'x': '2017-01-07T21:00:00'}, {'y': 5, 'x': '2017-01-08T00:00:00'}, {'y': 16, 'x': '2017-01-08T07:00:00'}, {'y': 14, 'x': '2017-01-08T11:00:00'}, {'y': 21, 'x': '2017-01-09T04:00:00'}, {'y': 25, 'x': '2017-01-09T20:00:00'}, {'y': 9, 'x': '2017-01-10T15:00:00'}, {'y': 25, 'x': '2017-01-11T10:00:00'}, {'y': 17, 'x': '2017-01-11T17:00:00'}, {'y': 10, 'x': '2017-01-12T11:00:00'}, {'y': 7, 'x': '2017-01-12T17:00:00'}, {'y': 11, 'x': '2017-01-12T22:00:00'}, {'y': 2, 'x': '2017-01-13T04:00:00'}, {'y': 13, 'x': '2017-01-13T12:00:00'}, {'y': 12, 'x': '2017-01-14T12:00:00'}, {'y': 16, 'x': '2017-01-15T10:00:00'}, {'y': 15, 'x': '2017-01-16T00:00:00'}, {'y': 23, 'x': '2017-01-16T17:00:00'}, {'y': 15, 'x': '2017-01-17T02:00:00'}, {'y': 22, 'x': '2017-01-17T12:00:00'}, {'y': 18, 'x': '2017-01-17T15:00:00'}, {'y': 16, 'x': '2017-01-18T14:00:00'}, {'y': 7, 'x': '2017-01-19T09:00:00'}, {'y': 10, 'x': '2017-01-20T02:00:00'}, {'y': 7, 'x': '2017-01-20T13:00:00'}, {'y': 5, 'x': '2017-01-20T17:00:00'}, {'y': 15, 'x': '2017-01-20T20:00:00'}, {'y': 5, 'x': '2017-01-21T06:00:00'}, {'y': 13, 'x': '2017-01-21T18:00:00'}, {'y': 20, 'x': '2017-01-22T13:00:00'}, {'y': 20, 'x': '2017-01-22T16:00:00'}, {'y': 23, 'x': '2017-01-23T15:00:00'}, {'y': 3, 'x': '2017-01-23T20:00:00'}, {'y': 20, 'x': '2017-01-24T15:00:00'}, {'y': 19, 'x': '2017-01-24T16:00:00'}, {'y': 1, 'x': '2017-01-25T00:00:00'}, {'y': 3, 'x': '2017-01-25T02:00:00'}, {'y': 22, 'x': '2017-01-25T23:00:00'}, {'y': 6, 'x': '2017-01-26T19:00:00'}, {'y': 17, 'x': '2017-01-27T10:00:00'}, {'y': 7, 'x': '2017-01-28T09:00:00'}, {'y': 23, 'x': '2017-01-29T05:00:00'}, {'y': 19, 'x': '2017-01-29T17:00:00'}, {'y': 16, 'x': '2017-01-30T08:00:00'}, {'y': 19, 'x': '2017-01-30T09:00:00'}, {'y': 23, 'x': '2017-01-31T06:00:00'}, {'y': 18, 'x': '2017-02-01T05:00:00'}]
        data_line = [{'y': 20, 'x': '2017-01-02T00:00:00'}, {'y': 3, 'x': '2017-01-03T00:00:00'}, {'y': 2, 'x': '2017-01-04T00:00:00'}, {'y': 18, 'x': '2017-01-05T00:00:00'}, {'y': 19, 'x': '2017-01-06T00:00:00'}, {'y': 20, 'x': '2017-01-07T00:00:00'}, {'y': 5, 'x': '2017-01-08T00:00:00'}, {'y': 23, 'x': '2017-01-09T00:00:00'}, {'y': 18, 'x': '2017-01-10T00:00:00'}, {'y': 5, 'x': '2017-01-11T00:00:00'}, {'y': 6, 'x': '2017-01-12T00:00:00'}, {'y': 2, 'x': '2017-01-13T00:00:00'}, {'y': 23, 'x': '2017-01-14T00:00:00'}, {'y': 3, 'x': '2017-01-15T00:00:00'}, {'y': 24, 'x': '2017-01-16T00:00:00'}, {'y': 10, 'x': '2017-01-17T00:00:00'}, {'y': 9, 'x': '2017-01-18T00:00:00'}, {'y': 11, 'x': '2017-01-19T00:00:00'}, {'y': 10, 'x': '2017-01-20T00:00:00'}, {'y': 2, 'x': '2017-01-21T00:00:00'}, {'y': 16, 'x': '2017-01-22T00:00:00'}, {'y': 24, 'x': '2017-01-23T00:00:00'}, {'y': 3, 'x': '2017-01-24T00:00:00'}, {'y': 13, 'x': '2017-01-25T00:00:00'}, {'y': 7, 'x': '2017-01-26T00:00:00'}, {'y': 10, 'x': '2017-01-27T00:00:00'}, {'y': 7, 'x': '2017-01-28T00:00:00'}, {'y': 13, 'x': '2017-01-29T00:00:00'}, {'y': 1, 'x': '2017-01-30T00:00:00'}, {'y': 10, 'x': '2017-01-31T00:00:00'}, {'y': 7, 'x': '2017-02-01T00:00:00'}]

        return [
            DataSet(type='line',
                    label='Scatter',
                    showLine=False,
                    data=data_scatter),
            DataSet(type='line',
                    label='Line',
                    borderColor='red',
                    data=data_line)
        ]


class BarChart(Chart):
    chart_type = 'bar'

    def get_labels(self, **kwargs):
        return bar_chart_x_labels

    def get_datasets(self, **kwargs):
        data = bar_chart_y_labels
        colors = bar_chart_colors

        return [DataSet(label='Bar Chart',
                        data=data,
                        borderWidth=1,
                        backgroundColor=colors,
                        borderColor=colors)]


class RadarChart(Chart):
    chart_type = 'radar'

    def get_labels(self):
        return ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"]

    def get_datasets(self, **kwargs):
        return [DataSet(label="My First dataset",
                        color=(179, 181, 198),
                        data=[65, 59, 90, 81, 56, 55, 40]),
                DataSet(label="My Second dataset",
                        color=(255, 99, 132),
                        data=[28, 48, 40, 19, 96, 27, 100])
               ]


class PolarChart(Chart):
    chart_type = 'polarArea'

    def get_labels(self, **kwargs):
        return bar_chart_x_labels

    def get_datasets(self, **kwargs):
        return [DataSet(label="My DataSet",
                        data=bar_chart_y_labels,
                        backgroundColor=bar_chart_colors)
                ]


class PieChart(Chart):
    chart_type = 'pie'

    def get_labels(self, **kwargs):
        return bar_chart_x_labels

    def get_datasets(self, **kwargs):
        data = bar_chart_y_labels
        colors = bar_chart_colors
        return [DataSet(data=data,
                        label="My Pie Data",
                        backgroundColor=colors,
                        hoverBackgroundColor=colors)]


class BubbleChart(Chart):
    chart_type = 'bubble'

    def get_datasets(self, **kwargs):
        data = [{
            'x': randint(1, 10),
            'y': randint(1, 25),
            'r': randint(1, 10),
        } for i in range(25)]

        return [DataSet(label="First DataSet",
                        data=data,
                        backgroundColor='#FF6384',
                        hoverBackgroundColor='#FF6384')]