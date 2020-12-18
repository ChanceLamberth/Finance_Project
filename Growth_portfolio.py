from yahoo_fin.stock_info import get_live_price

def portfolio_mkt_value(stocks, shares, target):
    # d_stock_shares = dict(zip(stocks, shares))
    
    mkt_value = 0
    stock_value = []
    for i in range(len(stocks)):
        l = get_live_price(stocks[i])
        mkt_value += l * shares[i]
        value = l * shares[i]
        stock_value.append(value)
    allocation = []
    for i in range(len(stock_value)):
        percentage = (stock_value[i] / mkt_value) * 100
        percent = round(percentage, 3)
        allocation.append(percent)
    allocation = dict(zip(stocks, allocation))
    target = dict(zip(stocks, target))
    a = round(mkt_value, 3)
    b = allocation
    c = target
    return "\n" + f"Market value: ${a}" + "\n" + f"stock allocation(%): {b}" + "\n" + f"          target(%): {c}"

def price(stocks, shares):
    price = []
    for i in range(len(stocks)):
        l = round(get_live_price(stocks[i]), 3)
        price.append(l)
    stock_price = dict(zip(stocks, price))
    stock_shares = dict(zip(stocks, shares))
    return f"              price: {stock_price}" + "\n" + f"             shares: {stock_shares}"


def main():
    stocks = ["SGOL", "VBR", "VGLT", "VGSH", "VOO"]
    shares = [40.000, 7.153, 7.155, 16.228, 4.018]
    target = [13.740, 0.000, 13.450, 10.000, 62.810]
    print(portfolio_mkt_value(stocks, shares, target))
    print(price(stocks, shares))


main()

"""

#Make program and file are in same folder
#change terminal so we are operating in folder
import pandas
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
pan = pandas.__version__
style.use("ggplot")

#uploaded CSV file successfully - trying to figure out how to manipulate date and value....
df = pandas.read_csv("history_work.csv")
print(df)

"""