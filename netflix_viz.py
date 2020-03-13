from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.ticker as mtick

# format for USD
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
# format for USD.00
fmt2 = '{x:,.2f}cents'
tick2 = mtick.StrMethodFormatter(fmt2)
# format for Billion USD.00
fmt3 = '${x:,.0f}B'
tick3 = mtick.StrMethodFormatter(fmt3)
# import data
netflix_stocks = pd.read_csv('NFLX.csv')
dowjones_stocks = pd.read_csv('DJI.csv')
netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')

# housekeeping
print (netflix_stocks.Date.max())
for df,df_name in zip([netflix_stocks,netflix_stocks_quarterly,dowjones_stocks],['netflix_stocks','netflix_stocks_quarterly','dowjones_stocks']):
    globals()[df_name] = df.rename(columns = {"Adj Close":"Price"}).reset_index()
# ______________________________________________________________________________
# Distribution of 2017 Netflix Stock Prices by Quarter
# ----------------------------------------------------

# get percentage median increase
print(netflix_stocks_quarterly.Price[netflix_stocks_quarterly['Quarter'] == 'Q4'].median() / netflix_stocks_quarterly.Price[netflix_stocks_quarterly['Quarter'] == 'Q1'].median())
# get  median increase
print(netflix_stocks_quarterly.Price[netflix_stocks_quarterly['Quarter'] == 'Q4'].median() - netflix_stocks_quarterly.Price[netflix_stocks_quarterly['Quarter'] == 'Q1'].median())
# get max and min prices
print(netflix_stocks_quarterly.Price[netflix_stocks_quarterly['Quarter'] == 'Q4'].max())
print(netflix_stocks_quarterly.Price[netflix_stocks_quarterly['Quarter'] == 'Q1'].min())
# get std deviation of Q3
print(netflix_stocks_quarterly.Price[netflix_stocks_quarterly['Quarter'] == 'Q3'].std())

# Violin Plot
sns.set_palette("muted")
sns.set_style("darkgrid")
ax1 = sns.violinplot(x = 'Quarter',y = 'Price',data = netflix_stocks_quarterly)
ax1.set_title("Distribution of 2017 Netflix Stock Prices by Quarter")
ax1.set(ylabel = 'Closing Stock Price', xlabel='Business Quarters in 2017')
ax1.yaxis.set_major_formatter(tick) 
plt.savefig('NFLX_StockPrice_Distribution.png')
plt.show()

# _____________________________________________________
# Earnings Per Share by Quarter
# ------------------------------

x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]
ax = plt.subplot()
ax.scatter(x_positions, earnings_actual, color = 'red', alpha=0.5)
ax.scatter(x_positions, earnings_estimate, color = 'blue', alpha=0.5)
plt.legend(['Actual', 'Estimate'])
plt.xticks(x_positions, chart_labels)
ax.set_title('Earnings Per Share by Quarter')
ax.set_xlabel("Quarter")
ax.set_ylabel("Earnings per share (cents)")
plt.savefig('EarningsPerShare.png')
plt.show()


# _____________________________________________________
# Revenue v. Earnings by Quarter
# ------------------------------

# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]

# get earnings as a percentage of revenue and mean result
epr = [b/a for a,b in zip(revenue_by_quarter,earnings_by_quarter)]
print np.mean(epr)

# Plot
# --------------------------
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]
ax = plt.subplot()
ax.yaxis.set_major_formatter(tick3) 
# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]
ax.bar(bars1_x, revenue_by_quarter)

# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]
ax.bar(bars2_x, earnings_by_quarter)

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]
plt.legend(labels)
plt.title('Revenue v. Earnings by Quarter')
plt.xticks(middle_x, quarter_labels)
ax.set_xlabel("Quarter")
plt.savefig('Rev_X_Earnings.png')
plt.show()
# -------------------------------------


# _____________________________________________________
# Netflix vs Dow Jones stocks throughout 2017
# --------------------------------------


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
plt.subplots(1,2,figsize=(14,7))
# NETFLIX
ax2 = plt.subplot(1, 2, 2)
ax2.plot(netflix_stocks.Date,netflix_stocks.Price,color = '#E50914')
ax2.set_xlabel("Month")
ax2.set_ylabel("Stock Price")
ax2.set_xticklabels(months)
ax2.set_title("Netflix Stocks throughout 2017")
ax2.yaxis.set_major_formatter(tick) 

# DOW JONES
ax3 = plt.subplot(1, 2, 1)
ax3.set_xlabel("Month")
ax3.set_ylabel("Stock Price")
ax3.set_xticklabels(months)
ax3.plot(dowjones_stocks.Date,dowjones_stocks.Price)
ax3.set_title("Dow Jones Stocks throughout 2017")
ax3.yaxis.set_major_formatter(tick) 

# ADJUST & SAVE
plt.subplots_adjust(wspace=.5)
plt.savefig('Netflix_X_DowJ.png')
plt.show()



print (netflix_stocks_quarterly.head())
print (dowjones_stocks.head())
print (netflix_stocks.head())