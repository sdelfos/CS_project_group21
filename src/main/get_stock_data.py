import pandas_datareader.data as web
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def get_stock_data(start_time, end_time):
    # fetch Apple stock data from iex
    return web.DataReader('AAPL', 'iex', start_time, end_time)


# fetch data from now to 5 years back
end = datetime.now()
start = end - timedelta(days=365*5)
stock_data = get_stock_data(start, end)

# plot the retrieved data
plt.plot(stock_data.close.values)
plt.show()
