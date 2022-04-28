import streamlit as st

option = st.selectbox(
     'Stock Analysis',
     ('Amazon', 'Microsoft', 'Google', 'Apple'))

if option == 'Amazon':
  st.header("Amazon Stock Analysis")
  st.image('Amazon Stock Analysis\'s - Graph.jpeg', caption='Apple Stock Analysis Graph')
  st.image('Amazon Stock Analysis\'s - Data.jpeg', caption='Apple Stock Analysis Data')
elif option == 'Microsoft':
  st.header("Microsoft Stock Analysis")
elif option == 'Google':
  st.header("Google Stock Analysis")
else :
  st.header("Apple Stock Analysis")
  
  


