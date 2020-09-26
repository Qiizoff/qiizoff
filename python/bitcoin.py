# # https://www.binance.vision/ru/halving

import dash_html_components as html
import dash_core_components as dcc
import dash
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta


# Старт сети
time = datetime(2009, 1, 9, 0, 5, 30)
print("\nСтарт сети BTC:", time)
# Изначальный размер блока
block = 50
print("Размер блока:", block)
i = 0
btc = 0  # Кол-во BTC
first_h = 210000  # Халвинг на блоке 210к
second_h = 0  # Счетчик блоков кратный 210к
halving = 0  # Кол-во халвингов
x = []
y = []
while i <= first_h + second_h:
    time += timedelta(minutes=9, seconds=30)
    btc += block
    if i == first_h + second_h:
        second_h += 210000
        halving += 1
        push = x.append
        push(halving)
        print('x:', x)
        print("\nХалвинг №:", halving)
        print("Дата:", time)
        block = block/2
        print("Размер блока:", block)
        print("Блоков за время:", 210000*block)
        print("Эмиссия BTC:", btc)
        push = y.append
        push(round(btc))
        print('y:', y)
        print("Халвинг на блоке:", second_h)
        if btc >= 21000000:
            break
    i += 1

# fig = go.Figure(data=go.Scatter(x=x, y=y))
# fig.show()


# -*- coding: utf-8 -*-

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x, 'y': y, 'type': 'bar', 'name': 'SF'},
                {'x': x, 'y': y,
                    'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)
