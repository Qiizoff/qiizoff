# # https://www.binance.vision/ru/halving
# python3 -m pip install plotly

import dash_html_components as html
import dash_core_components as dcc
import dash
# import plotly.graph_objects as go
# import numpy as np
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
x = [0]
y = [0]
y1 = [50]
y2 = [10500000]
while i <= first_h + second_h:
    time += timedelta(minutes=9, seconds=30)
    btc += block
    if i == first_h + second_h:
        halving += 1
        print("\nХалвинг №:", halving)
        print("Дата:", time)
        block = block/2
        print("Размер блока:", block)
        push = y1.append
        push(block)
        btctime=210000*block
        print("BTC за халвинг:", btctime)
        push = y2.append
        push(round(btctime))
        print("Эмиссия BTC:", btc)
        push = y.append
        push(round(btc))
        push = x.append
        push(halving)
        second_h += 210000
        print("Халвинг на блоке:", second_h)
    if btc >= 21000000:
        break
    i += 1

# fig = go.Figure(data=go.Scatter(x=x, y=y))
# fig.show()
print('\nХалвинг:', x)
print('\nЭмиссия BTC:', y)
print('\nРазмер блока:', y1)
print('\nBTC за халвинг:', y2)

# -*- coding: utf-8 -*-

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='BTC Graph'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x, 'y': y, 'type': 'bar', 'name': 'Эмиссия BTC'},
                {'x': x, 'y': y1, 'type': 'bar', 'name': u'Размер блока'},
                {'x': x, 'y': y2, 'type': 'bar', 'name': u'BTC за время'},
            ],
            'layout': {
                'title': 'BTC Halving Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)
