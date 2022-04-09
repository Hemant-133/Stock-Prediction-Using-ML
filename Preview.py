import streamlit as st

option = st.selectbox(
     'Stock Analysis',
     ('Amazon', 'Microsoft', 'Google', 'Apple'))

if option == 'Amazon':
  st.header("Amazon Stock Analysis")
  #st.image(image, caption='Sunrise by the mountains')
elif option == 'Microsoft':
  st.header("Microsoft Stock Analysis")
elif option == 'Google':
  st.header("Google Stock Analysis")
else :
  st.header("Apple Stock Analysis")
  
  


