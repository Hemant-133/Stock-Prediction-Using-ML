import streamlit as st

option = st.selectbox(
     'How would you like to be contacted?',
     ('Amazon', 'Microsoft', 'Google', 'Apple'))

if option == 'Amazon':
  st.header("Amazon Stock Analysis")
else if option == 'Microsoft':
  st.header("Microsoft Stock Analysis")
else if option == 'Google':
  st.header("Google Stock Analysis")
else if option == 'Apple':
  st.header("Apple Stock Analysis")
  
  


