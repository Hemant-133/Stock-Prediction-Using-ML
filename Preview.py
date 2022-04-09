import streamlit as st

option = st.selectbox(
     'How would you like to be contacted?',
     ('Amazon', 'Microsoft', 'Google', 'Apple'))

if option == 'Amazon':
  st.header("Amazon Stock Analysis")
elif option == 'Microsoft':
  st.header("Microsoft Stock Analysis")
elif option == 'Google':
  st.header("Google Stock Analysis")
else :
  st.header("Apple Stock Analysis")
  
  


