import streamlit as st

option = st.selectbox(
     'Stock Analysis',
     ('Amazon', 'Microsoft', 'Google', 'Apple'))

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
else :
  st.header("Apple Stock Analysis")
  st.image('Apple Stock Analysis\'s - Graph.jpeg', caption='Apple Stock Analysis Graph')
  st.image('Apple Stock Analysis\'s - Data.jpeg', caption='Apple Stock Analysis Data')
  
  


