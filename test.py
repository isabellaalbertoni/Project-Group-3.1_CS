import streamlit as st

st.write("we connected everything:)")

list_1 = [i for i in range(10) if i % 2 == 0]
st.write(list_1)