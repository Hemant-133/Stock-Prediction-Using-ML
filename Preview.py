import streamlit as st

option = st.selectbox(
     'Stock Analysis',
     ('Home','Amazon', 'Microsoft', 'Google', 'Apple'))

if option == 'Amazon':
  st.header("Amazon Stock Analysis")
  st.image('Amazon Stock Analysis\'s - Graph.jpeg', caption='Amazon Stock Analysis Graph')
  st.image('Amazon Stock Analysis\'s - Data.jpeg', caption='Amazon Stock Analysis Data')
elif option == 'Microsoft':
  st.header("Microsoft Stock Analysis")
  st.image('Microsoft Stock Analysis\'s - Graph.jpeg', caption='Microsoft Stock Analysis Graph')
  st.image('Microsoft Stock Analysis\'s - Data.jpeg', caption='Microsoft Stock Analysis Data')
elif option == 'Google':
  st.header("Google Stock Analysis")
  st.image('Google Stock Analysis\'s - Graph.jpeg', caption='Google Stock Analysis Graph')
  st.image('Google Stock Analysis\'s - Data.jpeg', caption='Google Stock Analysis Data')
elif option == 'Home':
     st.header("What Is Stock Analysis?")
     st.write("Stock analysis is the evaluation of a particular trading instrument, an investment sector, or the market as a whole. Stock analysts attempt to determine the future activity of an instrument, sector, or market.")
     st.subheader("Advantages of analysis of stock")
     st.write("When analyzing the chart, you place more importance on herd psychology (the market) than on the valuation of a publicly traded company. In fact, this is one of the advantages of technical analysis. To properly read the chart, you don't need to have any particular knowledge of economics, finance or accounting. Indeed, this type of analysis ignores fundamental data and focuses your attention on fluctuations in the share price as well as on trading volume. Understanding and applying technical analysis has nothing to do with your ability to assess a company's financial health.")
     st.write("Another advantage of interpreting charts is that this practice allows you to identify buy and sell signals in order to improve the timing when you take positions. Technical analysis can be more effective than fundamental analysis in determining the best time to buy or sell a stock. For example, using different financial ratios, fundamental analysis can help you determine whether a publicly traded company is undervalued or overvalued by the market. On the other hand, reading this accounting data does not really allow you to anticipate where the share price is headed over the short term")
     st.image('Graph.jpeg',caption = 'Graph Data')
     st.write("BLUE LINE : It is the previous value of stock plotted from the date/year  given below .")
     st.write("RED LINE : It is present value of stock and used for checking the accuracy of the analysis .")
     st.write("YELLOW LINE : It is the predicted value of a particular stock which has been plotted on the graph .")
     
else :
  st.header("Apple Stock Analysis")
  st.image('Apple Stock Analysis\'s - Graph.jpeg', caption='Apple Stock Analysis Graph')
  st.image('Apple Stock Analysis\'s - Data.jpeg', caption='Apple Stock Analysis Data')
  
  


