# # https://www.binance.vision/ru/halving
import plotly.graph_objects as go
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


fig = go.Figure(
    data=[go.Bar(x=x, y=y)],
    layout=go.Layout(
        title=go.layout.Title(text="BTC")
    )
)

fig.show()
