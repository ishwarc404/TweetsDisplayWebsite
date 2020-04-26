import pandas as pd 
import streamlit as st

df = pd.read_csv("Predictions.csv")
st.line_chart(df)