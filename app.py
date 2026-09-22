import streamlit as st
from src.data_loader import load_data

st.set_page_config(
    page_title="Olist Business Intelligence",
    layout="wide"
)

st.title("Olist Business Intelligence Dashboard")

data = load_data()

st.success("Data loaded successfully!")

for name, df in data.items():
    st.subheader(name)
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])