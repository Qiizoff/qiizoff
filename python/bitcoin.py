# # https://www.binance.vision/ru/halving

from datetime import datetime, timedelta

start_btc = datetime(2009, 1, 9, 0, 5, 30)
print("\nСтарт сети BTC:", start_btc)
block = 50
print("Размер блока:", block)
time_btc = start_btc
i = 0
btc = 0
first_h = 210000
second_f = 0
hardfork = 0
while i <= first_h + second_f:
    time_btc += timedelta(minutes=9, seconds=30)
    btc += block
    if i == first_h + second_f:
        hardfork += 1
        print("\nХардфорк №:", hardfork)
        print("Дата:", time_btc)
        block = block/2
        print("Размер блока:", block)
        print("Блоков за время:", 210000*block)
        print("Эмиссия BTC:", btc)
        second_f += 210000
        print("Хардфорк на блоке:", second_f)
        if btc >= 21000000:
            break
    i += 1
