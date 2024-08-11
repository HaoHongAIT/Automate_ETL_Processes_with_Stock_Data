import streamlit as st

st.set_page_config(
    page_title="Stock Prediction App",
    page_icon="",
)
with open('./data/document/main.md', 'r', encoding='utf-8') as file:
    markdown_content = file.read()
st.markdown(markdown_content)
