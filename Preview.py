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
else :
  st.header("Apple Stock Analysis")
  st.image('Apple Stock Analysis\'s - Graph.jpeg', caption='Apple Stock Analysis Graph')
  st.image('Apple Stock Analysis\'s - Data.jpeg', caption='Apple Stock Analysis Data')
  
  


