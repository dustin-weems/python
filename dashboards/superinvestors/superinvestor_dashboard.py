import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import squarify
import streamlit as st


def remove(string):
    return "".join(string.split())

# set page width to wide layout
st.set_page_config(layout="wide")

# add title and describe dashboard
st.title('Superinvestor Dashboard :bar_chart:')
st.caption(
    '''
    This dashboard includes US portfolio allocations from a select group of investors.  The data is sourced from 
    [dataroma](https://www.dataroma.com/m/home.php).  The underlying data aids my research process when hunting for new 
    investment ideas.  
    
    If multiple allocations exist under a 1% weighting, they will be combined into a "<1% basket". It is worth 
    emphasizing that investments on non-US stock exchanges have been excluded.  As a result, the percentage 
    allocations can be misleading.  For example, Mohnish Pabrai holds several positions listed outside of the US, so 
    his 2022Q4 portfolio appears heavily weighted towards a single US holding when that is not the case.   
    '''
)

# import data
df = pd.read_csv('https://github.com/dustin-weems/python/blob/main/dashboards/superinvestors/data/superinvestor_data_2022Q4.csv')
bio_df = pd.read_csv('https://github.com/dustin-weems/python/blob/main/dashboards/superinvestors/data/investor_bios.csv')

# add header for new section about latest holdings
st.markdown('---')
st.markdown('## Latest Holdings :chart_with_upwards_trend:')
st.caption(
    '''
    This section summarizes the latest holdings by investor.  In future versions of this dashboard, I will retain prior
    13F filings to allow the user to review older portfolio allocations.
    '''
)

# format portfolio allocation columns for better display in treemap plot
df['pct_of_portfolio'] = (df['pct_of_portfolio'] / 100).round(4)
df['%_of_portfolio'] = round((df.pct_of_portfolio * 100), 1).astype(str) + '%'

# add two columns for formatting drop-down boxes
col1, col2 = st.columns([2, 2])

# add drop-down selection box for investor name; default to Guy Spier
investor = col1.selectbox('Select Investor', df.investor_name.unique(), index=19)

# add drop-down selection box for time period
time_period = col2.selectbox(
    'Select Quarter', df[df['investor_name'] == investor].quarter.sort_values(ascending=False).unique()
)

# add investor bio
investor_bio = bio_df[bio_df['investor_name'] == investor].reset_index(drop=True).bio[0]
st.caption(investor_bio)

# filter original data and store in a new dataframe for treemap plot
df2 = df[(df['investor_name'] == investor) & (df['quarter'] == time_period)]

# create new column layout for plot formatting
col2_1, col2_2, col2_3 = st.columns([1, 3, 1])

# create treemap plot
fig, ax = plt.subplots()
fig.set_size_inches(12, 8)
squarify.plot(df2['pct_of_portfolio'], label=df2.stock_ticker, value=df2.pct_of_portfolio.map("{:.1%}".format),
              color=sns.color_palette('Set2'), pad=1, alpha=0.5, ax=ax, text_kwargs={'fontsize': 10})
plt.axis('off')
plt.title(investor + "'s " + remove(time_period) + " Portfolio")
col2_2.pyplot(fig)

# add table with descriptions for stock tickers
col_names = ['stock_description', '%_of_portfolio']
col2_2.table(
    df[(df['investor_name'] == investor) & (df['quarter'] == time_period)][col_names].reset_index(drop=True)
)

# add header for new section about books by listed investors
st.markdown('---')
st.markdown('## Library :books:')
st.caption(
    '''
    This section includes some wonderful books on investing, many of which were written by the investors included above.
    '''
)

st.markdown(
    '''
    * *The Intelligent Investor* by Benjamin Graham
    * *Common Stocks and Uncommon Profits* by Philip Fisher
    * *The Education of a Value Investor* by Guy Spier
    * *The Dhandho Investor* by Mohnish Pabrai
    * *The Warren Buffett Way* by Robert Hagstrom
    * *Investing for Growth* by Terry Smith
    * *Poor Charlie's Almanack* by Charlie Munger & Peter Kaufman
    '''
)

# add header for new section about online resources
st.markdown('---')
st.markdown('## Online Resources :computer:')
st.caption(
    '''
    This section includes some links to websites that I find helpful.  Aside from the books mentioned above, Warren
    Buffett's shareholder letters are an excellent resource for investing wisdom.  Dataroma provides the source data
    for the superinvestor data above.  Value Investors Club offers high quality write-ups on value-oriented investment 
    ideas, with superinvestors like Norbert Lou and Michael Burry having contributed in the past.  The remaining 
    resources have been helpful when digging into specific businesses, such as reviewing the past ten years of 
    high-level financial information and looking into recent insider purchases. 
    '''
)

st.markdown(
    '''
    * [Warren Buffett's Earlier Letters from Buffett Partnership Limited](https://www.ivey.uwo.ca/media/2975913/buffett-partnership-letters.pdf)
    * [Warren Buffett's Berkshire Hathaway Shareholder Letters](https://www.berkshirehathaway.com/letters/letters.html)
    * [Dataroma](https://www.dataroma.com/m/home.php)
    * [Value Investors Club](https://www.valueinvestorsclub.com/)
    * [QuickFS](https://quickfs.net/)
    * [Macrotrends](https://www.macrotrends.net/)
    * [OpenInsider](http://openinsider.com/)
    '''
)
